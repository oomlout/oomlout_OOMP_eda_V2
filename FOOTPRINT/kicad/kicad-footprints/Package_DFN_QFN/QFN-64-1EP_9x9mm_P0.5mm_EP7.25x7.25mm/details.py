
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm"
    hexID = "FZKDFNQFN641EP9X9P5EP725X725"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm', 'description': '64-Lead Plastic Quad Flat No-Lead Package, 9x9mm Body (see Atmel Appnote 8826)', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

