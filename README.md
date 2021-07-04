# UNESCO World Heritage Sites webmap using Python and Folium
#### In this project, I am using python as the base programming language and `main.py` as the center point of my app. I am using `pandas` to read and load my `worldheritage.csv` data file and I am using the package [folium](https://python-visualization.github.io/folium/docs-v0.6.0/) to dynamically create web maps. Folium allows us to manage our data in python and then helps us visualize it by using the [Leaflet.js](https://leafletjs.com/) library. This makes it super easy to build web maps in python without ever having to write any HTML, CSS, or Javascript code!

Upon opening `web_map.html`, the map is centered around Indore,Madhya Pradesh India (location at 22.747085659852694, 75.82918338870914). By iterating through my `worldheritage.csv` file which has relevant information about UNESCO World Heritage Sites in the world, I am able to plot markers at the exact location of every world heritage site with pop-up information about name of the site and hover to know the region in which it falls.The color of the marker is based on region in which the heritage site is located.The color are as indicated Orange for Africa, Red for Arab States, Light-Blue for Latin America and the Caribbean, Yellow for Europe and North America, Green for Asia and the Pacific

<img src="https://github.com/sidd8rth/world-heritage-sites-webmap/blob/main/Images/marker_layer.png"  />

On top of the marker layer, I added a polygon layer that color coated each country. The world country data is coming from `world.json` and the color of each country is based on the size of population. The color lightgreen signifies a country with a population less than 5 million people, green signifies a country with population between 5 and 10 million,yellow signifies a country with population between 10 and 20 million,orange signifies a country with population between 20 and 50 million, and any country with a population higher than 50 million is identified with the color red. I was able to accomplish this using a python `lambda` function along with `if/else` statements. 

```python
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor': 'lightgreen' if x['properties']['POP2005'] < 50000000
                            else 'green' if 50000000 <= x['properties']['POP2005'] < 100000000
                                                     else 'yellow' if 100000000 <= x['properties']['POP2005'] < 200000000
                                                     else 'orange' if 200000000 <= x['properties']['POP2005'] < 500000000
                                                     else 'red'}))
```

<img src="https://github.com/sidd8rth/world-heritage-sites-webmap/blob/main/Images/population_layer.png"  />

Lastly, I added layer control functionality to my map that allows me to turn the marker and population layer on and off also we can switch between various tiles from that toggler. This is located on the top right of my map.

<img src="https://github.com/sidd8rth/world-heritage-sites-webmap/blob/main/Images/complete_webmap.png" />
