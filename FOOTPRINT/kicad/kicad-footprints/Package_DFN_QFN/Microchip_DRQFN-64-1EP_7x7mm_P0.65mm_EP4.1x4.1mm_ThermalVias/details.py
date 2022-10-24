
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm_ThermalVias"
    hexID = "FZKDFNMCHIPDRQFN641EP7X7P65EP41X41THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm_ThermalVias', 'description': 'QFN, 64 Pin, dual row (http://ww1.microchip.com/downloads/en/DeviceDoc/64L_VQFN_7x7_Dual_Row_%5BSVB%5D_C04-21420a.pdf)', 'tags': 'QFN dual row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

