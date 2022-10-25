
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x2mm_P0.45mm_EP1.66x1.36mm"
    hexID = "FZKDFNDFN81EP3X2P45EP166X136"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x2mm_P0.45mm_EP1.66x1.36mm', 'description': 'DCB Package 8-Lead Plastic DFN (2mm x 3mm) (see Linear Technology DFN_8_05-08-1718.pdf)', 'tags': 'DFN 0.45', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x2mm_P0.45mm_EP1.66x1.36mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x2mm_P0.45mm_EP1.66x1.36mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

