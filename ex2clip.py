#Ex2-10
import arcpy

arcpy.env.workspace=("/Data/Exercise02")
arcpy.Clip_analysis("lakes.shp","basin.shp","Results/lakes_clip.shp")
arcpy.Clip_analysis("soils.shp","basin.shp","Results/soilsclip.shp")

