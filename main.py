import folium
import pandas as pd
data = pd.read_csv("worldheritage.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
name = list(data['NAME'])
region = list(data['REGION'])
html = """<h4>Heritage Site Information:</h4>
Name: %s 
"""


def marker_color(reg):
    if reg == "Africa":
        return "orange"
    elif reg == "Arab States":
        return "red"
    elif reg == "Latin America and the Caribbean":
        return "lightblue"
    elif reg == "Europe and North America":
        return "yellow"
    else:
        return "green"


# tiles changes the layer shown
web_map = folium.Map(location=[23.0, 0.0], tiles="Stamen Terrain", zoom_start=4)
folium.TileLayer('openstreetmap').add_to(web_map)
folium.TileLayer('cartodbpositron').add_to(web_map)
folium.TileLayer('cartodbdark_matter').add_to(web_map)
folium.TileLayer('stamentoner').add_to(web_map)
# Can be used to add various groups in one
fgs = folium.FeatureGroup(name="Heritage Sites")
# To add point layer
for lt, ln, name, reg in zip(lat, lon, name,region):
    iframe = folium.IFrame(html=html % name, width=250, height=80)
    fgs.add_child(folium.CircleMarker(location=(lt, ln), popup=folium.Popup(iframe), tooltip=folium.Tooltip(reg),
                                     fill_color=marker_color(reg), color="grey", fill_opacity=1, radius=8))
# To add polygon layer that is showing countries
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 100000000
                                                     else 'yellow' if 100000000 <= x['properties']['POP2005'] < 200000000
                                                     else 'orange' if 200000000 <= x['properties']['POP2005'] < 500000000
                                                     else 'red'}))
web_map.add_child(fgs)
web_map.add_child(fgp)
web_map.add_child(folium.LayerControl())
web_map.save("Map1.html")
