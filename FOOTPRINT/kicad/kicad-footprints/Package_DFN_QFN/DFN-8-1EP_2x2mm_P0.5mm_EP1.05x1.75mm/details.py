
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm"
    hexID = "FZKDFNDFN81EP2X2P5EP15X175"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm', 'description': 'DFN8 2x2, 0.5P; CASE 506CN (see ON Semiconductor 506CN.PDF)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

