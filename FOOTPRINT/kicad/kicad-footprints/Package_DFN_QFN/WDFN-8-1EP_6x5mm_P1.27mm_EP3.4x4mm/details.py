
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-8-1EP_6x5mm_P1.27mm_EP3.4x4mm"
    hexID = "FZKDFNWDFN81EP6X5P127EP34X4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-8-1EP_6x5mm_P1.27mm_EP3.4x4mm', 'description': 'WDFN, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_WDFN_5x6mm_MF_C04210B.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-8-1EP_6x5mm_P1.27mm_EP3.4x4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-8-1EP_6x5mm_P1.27mm_EP3.4x4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

