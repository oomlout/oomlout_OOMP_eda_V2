
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-28-1EP_4x4mm_P0.4mm_EP2.35x2.35mm_ThermalVias"
    hexID = "FZKDFNUQFN281EP4X4P4EP235X235THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-28-1EP_4x4mm_P0.4mm_EP2.35x2.35mm_ThermalVias', 'description': 'UQFN, 28 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=338), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-28-1EP_4x4mm_P0.4mm_EP2.35x2.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-28-1EP_4x4mm_P0.4mm_EP2.35x2.35mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

