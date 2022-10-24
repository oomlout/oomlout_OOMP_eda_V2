
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-6-1EP_3x3mm_P0.95mm"
    hexID = "FZKSONWSON61EP3X3P95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-6-1EP_3x3mm_P0.95mm', 'description': 'WSON6 3*3 MM, 0.95 PITCH; http://www.ti.com/lit/ds/symlink/lmr62421.pdf', 'tags': 'WSON6 0.95', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-6-1EP_3x3mm_P0.95mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-6-1EP_3x3mm_P0.95mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

