"""takes in a csv file, then creates a new csv file of paths between nodes and the distances"""
import argparse
import csv
import numpy as np

# work on
def normalize(edges):
    '''normalize the distances between the nodes'''
    # find the max distance
    max_distance = 0
    for edge in edges:
        if edge[2] > max_distance:
            max_distance = edge[2]
    # normalize the distances
    for edge in edges:
        edge[2] = edge[2]/max_distance



def main():
    '''takes in a csv file, then creates a new csv file of paths between nodes and the distances'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--inFile', required=True, type=str)
    parser.add_argument('--outFile', required=False, type=str)
    args = parser.parse_args()

    nodes=[]
    with open(args.inFile, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            nodes.append(row)

    edges = []
    for primary in nodes:
        for secondary in nodes:
            if primary != secondary:
                # make sure the path doesnt already exist
                if(primary[0]!="name" and secondary[0]!="name"):
                    magnitude = np.sqrt((float(primary[1])-float(secondary[1]))**2 +
                                        (float(primary[2])-float(secondary[2]))**2)
                    if [secondary[0], primary[0], magnitude] not in edges:
                        edges.append([primary[0], secondary[0], magnitude])

    normalize(edges)
    with open(args.outFile, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["node1", "node2", "distance"])
        writer.writerows(edges)


if __name__ =="__main__":
    main()
    