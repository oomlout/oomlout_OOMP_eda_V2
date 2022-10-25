
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-80_14x14mm_P0.65mm"
    hexID = "FZKQFPTQFP814X14P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-80_14x14mm_P0.65mm', 'description': '80-Lead Plastic Thin Quad Flatpack (PF) - 14x14x1 mm Body, 2.00 mm [TQFP] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-80_14x14mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-80_14x14mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

