
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PVQFN-N20_EP3.15x3.15mm_ThermalVias"
    hexID = "FZKDFNTEXASSPVQFNN2EP315X315THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PVQFN-N20_EP3.15x3.15mm_ThermalVias', 'description': 'QFN, 20 Pin (www.ti.com/lit/ds/symlink/tps7a7200.pdf#page=36), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PVQFN-N20_EP3.15x3.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PVQFN-N20_EP3.15x3.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

