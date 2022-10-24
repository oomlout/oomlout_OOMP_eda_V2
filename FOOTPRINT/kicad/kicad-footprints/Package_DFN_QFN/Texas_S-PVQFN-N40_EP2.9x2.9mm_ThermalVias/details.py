
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PVQFN-N40_EP2.9x2.9mm_ThermalVias"
    hexID = "FZKDFNTEXASSPVQFNN4EP29X29THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PVQFN-N40_EP2.9x2.9mm_ThermalVias', 'description': 'QFN, 40 Pin (http://www.ti.com/lit/ds/symlink/msp430fr5731.pdf#page=111 JEDEC MO-220 variation VJJD-2), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PVQFN-N40_EP2.9x2.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PVQFN-N40_EP2.9x2.9mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

