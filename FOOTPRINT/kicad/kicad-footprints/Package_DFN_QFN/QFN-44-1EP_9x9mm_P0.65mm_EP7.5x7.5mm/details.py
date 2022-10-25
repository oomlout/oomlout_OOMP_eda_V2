
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm"
    hexID = "FZKDFNQFN441EP9X9P65EP75X75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm', 'description': '44-Lead Plastic Quad Flat, No Lead Package - 9x9 mm Body [QFN]; see section 10.3 of https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf', 'tags': 'QFN 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

