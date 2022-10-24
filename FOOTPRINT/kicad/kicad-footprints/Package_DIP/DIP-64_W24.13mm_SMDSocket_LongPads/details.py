
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-64_W24.13mm_SMDSocket_LongPads"
    hexID = "FZKDIPDIP64W2413SMSOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-64_W24.13mm_SMDSocket_LongPads', 'description': '64-lead though-hole mounted DIP package, row spacing 24.13 mm (950 mils), SMDSocket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 24.13mm 950mil SMDSocket LongPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-64_W24.13mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-64_W24.13mm_SMDSocket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

