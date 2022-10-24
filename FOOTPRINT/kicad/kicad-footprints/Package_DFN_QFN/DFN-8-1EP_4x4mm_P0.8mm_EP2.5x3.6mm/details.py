
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm"
    hexID = "FZKDFNDFN81EP4X4P8EP25X36"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm', 'description': '8-Lead Plastic Dual Flat, No Lead Package (MD) - 4x4x0.9 mm Body [DFN] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

