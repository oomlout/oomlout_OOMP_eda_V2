
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "Battery_CR1225"
    hexID = "FZKBATBATCR1225"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Battery_CR1225', 'description': 'CR1225 battery', 'tags': 'battery CR1225 coin cell', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/Battery_CR1225.wrl', 'pins': {}})
    newPart['name'].append('Battery : Battery_CR1225')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

