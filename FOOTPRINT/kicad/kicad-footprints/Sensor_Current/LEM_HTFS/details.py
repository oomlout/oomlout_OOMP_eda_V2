
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "LEM_HTFS"
    hexID = "FZKSENCURRENTLEMHTFS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEM_HTFS', 'description': 'LEM HTFS x00-P current transducer (https://www.lem.com/sites/default/files/products_datasheets/htfs_200_800-p.pdf)', 'tags': 'HTFS current transducer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_HTFS.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Sensor_Current : LEM_HTFS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

