
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm_ThermalVias"
    hexID = "FZKDFNQFN761EP9X9P4EP38X38THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm_ThermalVias', 'description': 'QFN, 76 Pin (https://www.marvell.com/documents/bqcwxsoiqfjkcjdjhkvc/#page=19), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

