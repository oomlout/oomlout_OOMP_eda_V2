
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm"
    hexID = "FZKDFNDFN121EP2X3P45EP64X24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm', 'description': 'DDB Package; 12-Lead Plastic DFN (3mm x 2mm) (see Linear Technology DFN_12_05-08-1723.pdf)', 'tags': 'DFN 0.45', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

