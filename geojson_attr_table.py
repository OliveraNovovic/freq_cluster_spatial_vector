import json
from json import dump
import os
import pandas as pd


def attr_table(file, i):
    out_file = "cluster_" + str(i) + "_spatial_vector.csv"
    wfile = open(out_file, "w")
    wfile.write("land_use;area_km_2;frequency" + '\n')
    with open(file, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            land_use = feature['properties']['ITEM2012']
            area = feature['properties']['area_km_2']
            cluster_freq = feature['properties']['fpm_results_qgis_freq']
            wfile.write(land_use + ';' + str(area) + ';' + str(cluster_freq) + '\n')
            print(land_use, cluster_freq, area)
    wfile.close()


def attr_table2(file, i):
    out_file = "cluster_" + str(i) + "_poi_category_freq.csv"
    rows_list = []
    with open(file, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            amenity = feature['properties']['amenity']
            #print(amenity)
            rows_list.append(amenity)
    df = pd.DataFrame(rows_list)
    poi_freq = df[0].value_counts()
    poi_freq.to_csv(out_file)


def main():
    '''
    path = "/home/olivera/Documents/QGIS-graph-cores/Dissolved/"
    path2 = "/home/olivera/Documents/QGIS-graph-cores/Intersection/"
    for i in range(1, 12):
        #name = "UA2012-intersect-freq_cluster_" + str(i) + "-dissolve.geojson"
        name2 = "OSMpoints-intersect-freq_cluster_" + str(i) + ".geojson"
        file = path2 + name2
        print(file)
        #attr_table(file, i)
        #attr_table2(file, i)

    '''



    path3 = "/home/olivera/Documents/QGIS-graph-cores/Intersection/"
    name3 = "Milan_City_urban_POI.geojson"
    file3 = path3 + name3
    attr_table2(file3, 111) #111 means urban


if __name__ == '__main__':
    main()