#Ex2-10
import arcpy

arcpy.env.workspace=("Data/Exercise02")
arcpy.Clip_analysis("lakes.shp","basin.shp","Results/lakes_clip.shp")


