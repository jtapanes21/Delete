import arcpy

# A list of features and coordinate pairs
feature_info = [[[0,0], [0,1000], [1000, 0], [1000,1000]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Polygon objects
features = []

for feature in feature_info:
    # Create a Polygon object based on the array of points
    # Append to the list of Polygon objects
    features.append(
        arcpy.Polygon(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, r"D:\JHU\Spring 2019\Advanced Python Scripting for GIS\Exercise Data\Exercise08\polygons.shp")