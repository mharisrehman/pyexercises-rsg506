import arcpy
arcpy.env.workspace = "Data/Exercise02"
arcpy.Clip_analysis("soils.shp" , "basin.shp" , "Results/soil_clip.shp")

arcpy.Select_analysis("Results/soil_clip", "soil.shp", " FARMLNDCL='Not prime farmland'")