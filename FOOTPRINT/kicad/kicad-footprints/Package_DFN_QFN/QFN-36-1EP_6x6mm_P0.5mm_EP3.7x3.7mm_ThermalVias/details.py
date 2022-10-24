
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm_ThermalVias"
    hexID = "FZKDFNQFN361EP6X6P5EP37X37THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm_ThermalVias', 'description': 'QFN, 36 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/36L_QFN_6x6_with_3_7x3_7_EP_Punch_Dimpled_4E_C04-0241A.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

