from geoserver import GeoServer
from pathlib import Path

# Connect to a GeoServer instance
geoserver = GeoServer(
    service_url="http://139.59.221.224:8080/geoserver",
    username="admin",
    password="geoserver"
)



workspaces = geoserver.get_workspaces()
print(workspaces)

workspaces_name = 'ws_demo'

# if geoserver.workspace_exists(workspaces_name):
#     geoserver.delete_workspace(workspaces_name, recurse=True)

# geoserver.create_workspace_from_name(workspaces_name)

path = 'C:/Users/parin/QGIS_storage/raster/'
tiff = 'SV2-01-MUX-PAN.tif'
file_tiff = path+tiff
# Upload a GeoTIFF
geoserver.upload_coverage_store(file=file_tiff, format="geotiff", workspace=workspaces_name)
