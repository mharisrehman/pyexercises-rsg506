import arcpy
arcpy.env.workspace = "Data/Exercise02"

input_feature = "soils.shp"
clip_feature = "basin.shp"
clip_out="Results/soil_clip.shp"

clip=arcpy.Clip_analysis(input_feature,clip_feature,clip_out)

if clip_out is None: 
    print("Clip Error")
else:
    select=arcpy.Select_analysis(clip_out, "soil.shp", " FARMLNDCL='Not prime farmland'")

