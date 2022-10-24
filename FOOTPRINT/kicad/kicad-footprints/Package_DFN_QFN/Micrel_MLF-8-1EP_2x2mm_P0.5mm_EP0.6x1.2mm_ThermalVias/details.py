
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm_ThermalVias"
    hexID = "FZKDFNMICRELMLF81EP2X2P5EP6X12THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm_ThermalVias', 'description': 'Micrel  MLF, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/mic23050.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Micrel MLF NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.6x1.2mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

