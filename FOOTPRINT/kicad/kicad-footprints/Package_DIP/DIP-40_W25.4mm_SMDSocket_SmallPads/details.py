
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-40_W25.4mm_SMDSocket_SmallPads"
    hexID = "FZKDIPDIP4W254SMSOSLLPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-40_W25.4mm_SMDSocket_SmallPads', 'description': '40-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils), SMDSocket, SmallPads', 'tags': 'THT DIP DIL PDIP 2.54mm 25.4mm 1000mil SMDSocket SmallPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-40_W25.4mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-40_W25.4mm_SMDSocket_SmallPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

