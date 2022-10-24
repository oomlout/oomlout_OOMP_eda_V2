
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-12_W7.62mm_SMDSocket_SmallPads"
    hexID = "FZKDIPDIP12W762SMSOSLLPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-12_W7.62mm_SMDSocket_SmallPads', 'description': '12-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil SMDSocket SmallPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-12_W7.62mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-12_W7.62mm_SMDSocket_SmallPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

