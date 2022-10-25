
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias"
    hexID = "FZKDFNHVQFN241EP4X4P5EP26X26THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias', 'description': 'HVQFN, 24 Pin (https://www.nxp.com/docs/en/package-information/SOT616-3.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'HVQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

