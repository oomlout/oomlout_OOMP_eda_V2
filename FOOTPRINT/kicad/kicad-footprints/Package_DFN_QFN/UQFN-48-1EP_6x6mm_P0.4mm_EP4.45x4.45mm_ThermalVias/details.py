
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm_ThermalVias"
    hexID = "FZKDFNUQFN481EP6X6P4EP445X445THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm_ThermalVias', 'description': 'UQFN, 48 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=347), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'UQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

