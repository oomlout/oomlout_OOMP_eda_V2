
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-10-1EP_4x3mm_P0.5mm_EP2.2x2mm"
    hexID = "FZKSONWSON11EP4X3P5EP22X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-10-1EP_4x3mm_P0.5mm_EP2.2x2mm', 'description': '10-Lead Plastic WSON, 4x3mm Body, 0.5mm Pitch (http://www.ti.com/lit/ds/symlink/lm4990.pdf)', 'tags': 'WSON 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-10-1EP_4x3mm_P0.5mm_EP2.2x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-10-1EP_4x3mm_P0.5mm_EP2.2x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

