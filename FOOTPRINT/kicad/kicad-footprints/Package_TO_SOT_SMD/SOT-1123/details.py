
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "SOT-1123"
    hexID = "FZKPACKAGETOSOTSMSOT1123"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOT-1123', 'description': 'SOT-1123 small outline transistor (see http://www.onsemi.com/pub/Collateral/NST3906F3-D.PDF)', 'tags': 'SOT-1123 transistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-1123.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_TO_SOT_SMD : SOT-1123')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

