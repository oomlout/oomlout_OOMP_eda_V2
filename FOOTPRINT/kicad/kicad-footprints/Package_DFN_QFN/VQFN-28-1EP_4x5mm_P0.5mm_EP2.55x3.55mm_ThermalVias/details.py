
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm_ThermalVias"
    hexID = "FZKDFNVQFN281EP4X5P5EP255X355THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm_ThermalVias', 'description': 'VQFN, 28 Pin (http://www.ti.com/lit/ds/symlink/lm5175.pdf#page=40), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

