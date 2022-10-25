
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm_ThermalVias"
    hexID = "FZKDFNTDFN81EP3X2P5EP18X165THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm_ThermalVias', 'description': '8-lead plastic dual flat, 2x3x0.75mm size, 0.5mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_TDFN_2x3_MN_C04-0129E-MN.pdf)', 'tags': 'TDFN DFN 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

