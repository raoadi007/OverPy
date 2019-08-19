from urllib.request import urlopen
from time import sleep
from sys import exc_info
from xmltodict import parse
 
ids = [531300655]
for wayid in ids:
    try:
        response = urlopen('http://www.openstreetmap.org/api/0.6/way/{0}/full'.format(wayid))
        s = response.read()
        d = parse(s)
        way_nodes_coord = d['osm']['node']
        for j in way_nodes_coord:
            print("lat = {0}, lon = {1}".format(float(j['@lat']),float(j['@lon'])))
        for tag in d['osm']['way']['tag']:
            print("key = {0}, value = {1}".format(tag['@k'], tag['@v']))
        sleep(1)
    except:
        print("Got error for location {0}".format(wayid))
