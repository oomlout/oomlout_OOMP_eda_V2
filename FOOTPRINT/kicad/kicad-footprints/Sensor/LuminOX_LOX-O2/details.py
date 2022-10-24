
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "LuminOX_LOX-O2"
    hexID = "FZKSENLUMINOXLOXO2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LuminOX_LOX-O2', 'description': 'SST LuminOX Luminescence-based O2 sensor, https://sstsensing.com/wp-content/uploads/2021/08/DS0030rev15_LuminOx.pdf', 'tags': 'SST LuminOX O2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/LuminOX_LOX-O2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor : LuminOX_LOX-O2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

