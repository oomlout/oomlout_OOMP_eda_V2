
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm"
    hexID = "FZKDFNDFN81EP3X2P5EP175X145"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'description': '8-Lead Plastic Dual Flat, No Lead Package (MC) - 2x3x0.9 mm Body [DFN] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

