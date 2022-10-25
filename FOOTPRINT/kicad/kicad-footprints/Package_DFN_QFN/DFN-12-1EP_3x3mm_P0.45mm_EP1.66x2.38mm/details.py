
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm"
    hexID = "FZKDFNDFN121EP3X3P45EP166X238"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm', 'description': 'DD Package; 12-Lead Plastic DFN (3mm x 3mm) (see Linear Technology DFN_12_05-08-1725.pdf)', 'tags': 'DFN 0.45', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

