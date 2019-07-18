#! usr/bin/env python

from sys import argv
from os.path import exists
import simplejson as json 

script, in_file, out_file = argv

data = json.load(open(in_file))

usable = data["data"]["list"]

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lng"], d["lat"]],
            },
            "properties" : {"price": float(d["price"].replace("M","").replace("K","")),"id_listing": d["id_listing"],"house_type": d["house_type"]}
    }    for d in usable]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print(geojson)