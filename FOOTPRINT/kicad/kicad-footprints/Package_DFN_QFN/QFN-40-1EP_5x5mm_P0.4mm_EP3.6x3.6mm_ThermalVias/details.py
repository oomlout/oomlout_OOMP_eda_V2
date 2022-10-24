
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm_ThermalVias"
    hexID = "FZKDFNQFN41EP5X5P4EP36X36THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm_ThermalVias', 'description': 'QFN, 40 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=297), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

