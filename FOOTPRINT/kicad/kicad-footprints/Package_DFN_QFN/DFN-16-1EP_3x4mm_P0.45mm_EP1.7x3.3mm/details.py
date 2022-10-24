
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-16-1EP_3x4mm_P0.45mm_EP1.7x3.3mm"
    hexID = "FZKDFNDFN161EP3X4P45EP17X33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-16-1EP_3x4mm_P0.45mm_EP1.7x3.3mm', 'description': 'DE Package; 16-Lead Plastic DFN (4mm x 3mm) (see Linear Technology DFN_16_05-08-1732.pdf)', 'tags': 'DFN 0.45', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-16-1EP_3x4mm_P0.45mm_EP1.7x3.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-16-1EP_3x4mm_P0.45mm_EP1.7x3.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

