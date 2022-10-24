
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm"
    hexID = "FZKSONWSON81EP3X3P5EP16X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm', 'description': '8-Lead Plastic WSON, 2x2mm Body, 0.5mm Pitch, WSON-8, http://www.ti.com/lit/ds/symlink/lm27761.pdf', 'tags': 'WSON 8 1EP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

