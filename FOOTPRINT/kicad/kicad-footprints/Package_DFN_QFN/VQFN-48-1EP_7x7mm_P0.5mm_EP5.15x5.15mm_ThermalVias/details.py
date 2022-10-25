
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm_ThermalVias"
    hexID = "FZKDFNVQFN481EP7X7P5EP515X515THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm_ThermalVias', 'description': 'VQFN, 48 Pin (http://www.ti.com/lit/ds/symlink/cc1312r.pdf#page=48), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

