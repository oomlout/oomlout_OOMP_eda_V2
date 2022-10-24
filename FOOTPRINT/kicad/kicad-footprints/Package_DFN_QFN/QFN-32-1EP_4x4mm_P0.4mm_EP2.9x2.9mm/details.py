
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm"
    hexID = "FZKDFNQFN321EP4X4P4EP29X29"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm', 'description': 'QFN, 32 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-8153-8-and-16-bit-avr-microcontroller-xmega-e-atxmega8e5-atxmega16e5-atxmega32e5_datasheet.pdf#page=70), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

