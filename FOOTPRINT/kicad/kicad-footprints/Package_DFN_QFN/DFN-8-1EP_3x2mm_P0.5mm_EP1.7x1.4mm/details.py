
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x2mm_P0.5mm_EP1.7x1.4mm"
    hexID = "FZKDFNDFN81EP3X2P5EP17X14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x2mm_P0.5mm_EP1.7x1.4mm', 'description': 'DFN, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_DFN_2x3x0_9_MC_C04-123C.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x2mm_P0.5mm_EP1.7x1.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x2mm_P0.5mm_EP1.7x1.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

