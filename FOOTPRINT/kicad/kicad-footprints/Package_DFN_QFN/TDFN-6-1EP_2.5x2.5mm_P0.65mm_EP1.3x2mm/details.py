
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm"
    hexID = "FZKDFNTDFN61EP25X25P65EP13X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm', 'description': 'TDFN, 6 Pin (http://www.nve.com/Downloads/ab3.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

