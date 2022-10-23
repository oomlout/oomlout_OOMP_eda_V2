
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "OLED-128O064D"
    hexID = "FZKDIOL128O64D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OLED-128O064D', 'description': '128x64 OLED display', 'tags': 'display oled', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/OLED-128O064D.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Display : OLED-128O064D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

