"""extracts the points of interest from the kml file and writes them to a csv file"""
import argparse
from bs4 import BeautifulSoup

def main():
    """extracts the points of interest from the kml file and writes them to a csv file"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--kml', required=True, type=str)
    parser.add_argument('--output', required=True, type=str)
    args = parser.parse_args()
    # read the kml file
    with open(args.kml, 'r', encoding='utf-8') as file:
        kml = file.read()
    # parse the kml file
    soup = BeautifulSoup(kml, "xml")
    # extract the coordinates
    coordinates = [c.text for c in soup.find_all('coordinates')]
    # extract the names
    names = [n.text for n in soup.find_all('name')]
    # write the coordinates and names to a csv file
    with open(args.output, 'w',encoding='utf-8') as file:
        file.write('name,longitude,latitude\n')
        for name, coordinate in zip(names, coordinates):
            longitude, latitude, _ = coordinate.strip().split(',')
            file.write(f'{name},{longitude},{latitude}\n')

if __name__ == '__main__':
    main()
