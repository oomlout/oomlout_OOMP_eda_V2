
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Distance"
    oIndex = "ST_VL53L1x"
    hexID = "FZKSENDISTANCESTVL53L1X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_VL53L1x', 'description': 'VL53L1x distance sensor', 'tags': 'VL53L1CXV0FY1 VL53L1x', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Distance.3dshapes/ST_VL53L1x.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Distance : ST_VL53L1x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

