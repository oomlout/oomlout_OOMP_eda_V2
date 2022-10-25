
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-6-2EP_4.0x2.6mm_P0.65mm"
    hexID = "FZKDFNWDFN62EP4X26P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-6-2EP_4.0x2.6mm_P0.65mm', 'description': 'WDFN, 6 pin, 4.0x2.6, 0.65P; Two exposed pads, (https://www.onsemi.com/pub/Collateral/511BZ.PDF)', 'tags': 'DFN 0.65P dual flag', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-6-2EP_4.0x2.6mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-6-2EP_4.0x2.6mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

