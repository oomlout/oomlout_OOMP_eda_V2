
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm"
    hexID = "FZKDFNDFN141EP3X45P65EP165X425"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm', 'description': '14-lead very thin plastic quad flat, 3.0x4.5mm size, 0.65mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/14L_VDFN_4_5x3_0mm_JHA_C041198A.pdf)', 'tags': 'VDFN DFN 0.65mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-14-1EP_3x4.5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

