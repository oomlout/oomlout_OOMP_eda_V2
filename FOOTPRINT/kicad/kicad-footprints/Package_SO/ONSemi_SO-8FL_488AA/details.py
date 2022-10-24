
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "ONSemi_SO-8FL_488AA"
    hexID = "FZKSOONSEMISO8FL488AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ONSemi_SO-8FL_488AA', 'description': 'ON Semi DFN5 5x6mm 1.27P SO-8FL CASE 488A https://www.onsemi.com/pub/Collateral/488AA.PDF', 'tags': 'ON Semi DFN5 5x6mm 1.27P SO-8FL CASE 488A ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/ONSemi_SO-8FL_488AA.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : ONSemi_SO-8FL_488AA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

