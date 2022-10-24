
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm"
    hexID = "FZKDFNDFN61EP2X2P65EP1X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'description': '6-Lead Plastic Dual Flat, No Lead Package (MA) - 2x2x0.9 mm Body [DFN] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

