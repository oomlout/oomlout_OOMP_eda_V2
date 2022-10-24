
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-28_5.2x3.8mm_P0.5mm"
    hexID = "FZKLGALGA2852X38P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-28_5.2x3.8mm_P0.5mm', 'description': 'LGA 28 5.2x3.8mm Pitch 0.5mm', 'tags': 'LGA 28 5.2x3.8mm Pitch 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-28_5.2x3.8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_LGA : LGA-28_5.2x3.8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

