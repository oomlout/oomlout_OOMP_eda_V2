
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm"
    hexID = "FZKDFNVQFN281EP4X4P45EP24X24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm', 'description': 'VQFN, 28 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-9505-AT42-QTouch-BSW-AT42QT1060_Datasheet.pdf#page=28), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

