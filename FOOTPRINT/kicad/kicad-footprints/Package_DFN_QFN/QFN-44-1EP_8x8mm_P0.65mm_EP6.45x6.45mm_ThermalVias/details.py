
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm_ThermalVias"
    hexID = "FZKDFNQFN441EP8X8P65EP645X645THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm_ThermalVias', 'description': 'QFN, 44 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf#page=152), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

