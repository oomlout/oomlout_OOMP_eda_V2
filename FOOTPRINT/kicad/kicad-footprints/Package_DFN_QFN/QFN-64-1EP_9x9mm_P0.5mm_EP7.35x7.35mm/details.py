
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-64-1EP_9x9mm_P0.5mm_EP7.35x7.35mm"
    hexID = "FZKDFNQFN641EP9X9P5EP735X735"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-64-1EP_9x9mm_P0.5mm_EP7.35x7.35mm', 'description': '64-Lead Plastic Quad Flat, No Lead Package (MR) - 9x9x0.9 mm Body [QFN]; (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-64-1EP_9x9mm_P0.5mm_EP7.35x7.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-64-1EP_9x9mm_P0.5mm_EP7.35x7.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

