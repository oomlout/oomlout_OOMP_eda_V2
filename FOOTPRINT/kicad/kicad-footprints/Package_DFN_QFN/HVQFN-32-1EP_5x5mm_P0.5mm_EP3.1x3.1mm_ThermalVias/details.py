
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "HVQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias"
    hexID = "FZKDFNHVQFN321EP5X5P5EP31X31THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias', 'description': 'HVQFN, 32 Pin (https://www.nxp.com/docs/en/package-information/SOT617-1.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'HVQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/HVQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : HVQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

