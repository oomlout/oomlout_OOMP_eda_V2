
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-24L_3x3.5mm_P0.43mm"
    hexID = "FZKLGALGA24L3X35P43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-24L_3x3.5mm_P0.43mm', 'description': 'LGA 24L 3x3.5mm Pitch 0.43mm', 'tags': 'LGA 24L 3x3.5mm Pitch 0.43mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-24L_3x3.5mm_P0.43mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_LGA : LGA-24L_3x3.5mm_P0.43mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

