
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "SHT1x"
    hexID = "FZKSENSHT1X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SHT1x', 'description': 'SHT1x', 'tags': 'SHT1x', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Temperature.3dshapes/SHT1x.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor : SHT1x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

