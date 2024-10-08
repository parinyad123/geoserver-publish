# https://arthurdjn.github.io/geoserver-py/notebooks/Stores/#adding-an-existing-shapefile

from pathlib import Path
from geoserver import GeoServer
from geoserver.exceptions import GeoServerError
import os
import zipfile
from os import path
from zipfile import ZipFile

# Connect to a GeoServer instance
geoserver = GeoServer(
    service_url="http://138.197.163.159:8080/geoserver",
    username="admin",
    password="geoserver"
)

workspace_name = "demo_shapefile"
# Check if the workspace not exists create a workspace and a store.
if not geoserver.workspace_exists(workspace_name):
    # geoserver.delete_workspace(workspace_name, recurse=True)
    geoserver.create_workspace_from_name(workspace_name)

shapefile_name = "shape_polygon2"
# Directory containing sample data
DATA_DIR = "C:/Users/parin/QGIS_storage/vectors/"
shapefile_zip = DATA_DIR + shapefile_name + ".zip"
print(shapefile_zip)


# Check if the zip file not exists
if not os.path.exists(shapefile_zip):
    print(f"'{shapefile_name+".zip"}' does not exist.")
    file_extension = [
        ".cpg",
        ".dbf",
        ".prj",
        ".shp",
        ".shx"
    ]

    shapefile = [DATA_DIR+shapefile_name+i for i in file_extension]
    print(shapefile)
    # Create a ZIP file
    with zipfile.ZipFile(shapefile_zip, 'w') as zipf:
        for file in shapefile:
            # Check if the file exists before adding to ZIP
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))  # Write the file into the ZIP
    # with ZipFile(shapefile_zip, 'w') as zipObj:
    #     for file in shapefile:
    #         zipObj.write(file, path.basename(path.normpath(file)))


        


stored = geoserver.upload_data_store(file=shapefile_zip, workspace=workspace_name)
print("stored = ", stored)

Retrieving = geoserver.get_data_store(name=shapefile_name, workspace=workspace_name)
print("Retrieving = ", Retrieving)


