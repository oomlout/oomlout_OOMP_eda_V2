
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_ThermalVias"
    hexID = "FZKDFNUQFN21EP4X4P5EP28X28THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_ThermalVias', 'description': 'UQFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/40001839B.pdf#page=464), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

