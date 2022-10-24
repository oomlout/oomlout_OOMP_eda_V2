
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm"
    hexID = "FZKDFNWDFN81EP4X3P65EP24X18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm', 'description': 'WDFN, 8 Pin (https://www.onsemi.com/pub/Collateral/509AF.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

