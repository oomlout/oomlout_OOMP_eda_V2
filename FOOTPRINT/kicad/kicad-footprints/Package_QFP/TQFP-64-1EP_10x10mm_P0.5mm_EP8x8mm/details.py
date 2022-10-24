
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm"
    hexID = "FZKQFPTQFP641EP1X1P5EP8X8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm', 'description': '64-Lead Plastic Thin Quad Flatpack (PT) - 10x10x1 mm Body, 2.00 mm Footprint [TQFP] thermal pad', 'tags': 'QFP 0.5 ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-64_10x10mm_P0.5mm_EP8x8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

