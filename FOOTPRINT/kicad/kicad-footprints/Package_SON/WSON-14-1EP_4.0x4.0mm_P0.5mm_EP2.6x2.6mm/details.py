
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-14-1EP_4.0x4.0mm_P0.5mm_EP2.6x2.6mm"
    hexID = "FZKSONWSON141EP4X4P5EP26X26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-14-1EP_4.0x4.0mm_P0.5mm_EP2.6x2.6mm', 'description': '14-Lead Plastic Dual Flat, No Lead Package - 4.0x4.0x0.8 mm Body [WSON], http://www.ti.com/lit/ml/mpds421/mpds421.pdf', 'tags': 'NHL014B', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-14-1EP_4.0x4.0mm_P0.5mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-14-1EP_4.0x4.0mm_P0.5mm_EP2.6x2.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

