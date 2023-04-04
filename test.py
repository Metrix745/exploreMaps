"""this is a test file to see if the google maps api works"""

#import the google maps api and have it process the area of University of Maryland, Baltimore County
import gmplot
#set up the map
gmap = gmplot.GoogleMapPlotter(39.254, -76.711, 16)
#set up the heatmap
gmap.heatmap( [39.254, 39.254, 39.254, 39.254], [-76.711, -76.711, -76.711, -76.711] )
#draw the map
gmap.draw( "mymap.html" )

#now extract the outlines of all the buildings on campus
