
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm"
    hexID = "FZKDFNWDFN81EP3X2P5EP13X14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm', 'description': 'WDFN, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_TDFN_2x3_MNY_C04-0129E-MNY.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

