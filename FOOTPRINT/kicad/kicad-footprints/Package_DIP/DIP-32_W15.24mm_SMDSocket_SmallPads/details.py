
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-32_W15.24mm_SMDSocket_SmallPads"
    hexID = "FZKDIPDIP32W1524SMSOSLLPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-32_W15.24mm_SMDSocket_SmallPads', 'description': '32-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads', 'tags': 'THT DIP DIL PDIP 2.54mm 15.24mm 600mil SMDSocket SmallPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-32_W15.24mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-32_W15.24mm_SMDSocket_SmallPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

