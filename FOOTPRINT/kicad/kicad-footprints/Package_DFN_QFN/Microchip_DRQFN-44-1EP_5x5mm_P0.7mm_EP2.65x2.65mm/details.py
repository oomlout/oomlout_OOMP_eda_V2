
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm"
    hexID = "FZKDFNMCHIPDRQFN441EP5X5P7EP265X265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm', 'description': 'QFN, 44 Pin, dual row (http://ww1.microchip.com/downloads/en/DeviceDoc/44L_VQFN_5x5mm_Dual_Row_%5BS3B%5D_C04-21399a.pdf)', 'tags': 'QFN dual row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

