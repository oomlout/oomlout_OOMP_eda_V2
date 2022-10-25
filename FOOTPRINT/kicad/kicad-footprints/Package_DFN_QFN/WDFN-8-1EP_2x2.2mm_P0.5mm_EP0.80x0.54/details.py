
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-8-1EP_2x2.2mm_P0.5mm_EP0.80x0.54"
    hexID = "FZKDFNWDFN81EP2X22P5EP8X54"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-8-1EP_2x2.2mm_P0.5mm_EP0.80x0.54', 'description': 'https://www.onsemi.com/pub/Collateral/511BN.PDF', 'tags': 'WDFN-8 1EP 2.2X2.0 0.5P', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-8_2.2x2mm_P0.5mm_1EP.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-8-1EP_2x2.2mm_P0.5mm_EP0.80x0.54')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

