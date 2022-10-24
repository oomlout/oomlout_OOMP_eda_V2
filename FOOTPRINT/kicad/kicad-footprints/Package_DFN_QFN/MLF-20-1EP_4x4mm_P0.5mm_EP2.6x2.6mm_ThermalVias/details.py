
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias"
    hexID = "FZKDFNMLF21EP4X4P5EP26X26THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias', 'description': 'MLF, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf#page=263), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'MLF NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

