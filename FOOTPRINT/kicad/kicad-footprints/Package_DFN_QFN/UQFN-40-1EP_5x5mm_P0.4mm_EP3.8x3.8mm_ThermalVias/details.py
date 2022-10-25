
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-40-1EP_5x5mm_P0.4mm_EP3.8x3.8mm_ThermalVias"
    hexID = "FZKDFNUQFN41EP5X5P4EP38X38THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-40-1EP_5x5mm_P0.4mm_EP3.8x3.8mm_ThermalVias', 'description': 'UQFN, 40 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=345), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-40-1EP_5x5mm_P0.4mm_EP3.8x3.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-40-1EP_5x5mm_P0.4mm_EP3.8x3.8mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

