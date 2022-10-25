
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm"
    hexID = "FZKDFNDFN161EP3X5P5EP166X44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm', 'description': 'DHC Package; 16-Lead Plastic DFN (5mm x 3mm) (see Linear Technology DFN_16_05-08-1706.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

