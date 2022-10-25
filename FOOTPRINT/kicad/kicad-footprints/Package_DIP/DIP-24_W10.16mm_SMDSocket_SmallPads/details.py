
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-24_W10.16mm_SMDSocket_SmallPads"
    hexID = "FZKDIPDIP24W116SMSOSLLPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-24_W10.16mm_SMDSocket_SmallPads', 'description': '24-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils), SMDSocket, SmallPads', 'tags': 'THT DIP DIL PDIP 2.54mm 10.16mm 400mil SMDSocket SmallPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-24_W10.16mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-24_W10.16mm_SMDSocket_SmallPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

