
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm_ThermalVias"
    hexID = "FZKDFNVQFN241EP4X4P5EP245X245THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm_ThermalVias', 'description': 'VQFN, 24 Pin (http://www.ti.com/lit/ds/symlink/msp430f1101a.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

