
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-8-1EP_3x2mm_P0.5mm_EP1.4x1.4mm"
    hexID = "FZKDFNTDFN81EP3X2P5EP14X14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-8-1EP_3x2mm_P0.5mm_EP1.4x1.4mm', 'description': 'TDFN, 8 Pin (http://ww1.microchip.com/downloads/en/devicedoc/20005514a.pdf#page=35), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-8-1EP_3x2mm_P0.5mm_EP1.4x1.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-8-1EP_3x2mm_P0.5mm_EP1.4x1.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

