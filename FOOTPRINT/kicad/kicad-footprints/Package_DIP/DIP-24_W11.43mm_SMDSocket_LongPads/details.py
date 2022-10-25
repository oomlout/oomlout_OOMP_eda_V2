
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-24_W11.43mm_SMDSocket_LongPads"
    hexID = "FZKDIPDIP24W1143SMSOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-24_W11.43mm_SMDSocket_LongPads', 'description': '24-lead though-hole mounted DIP package, row spacing 11.43 mm (450 mils), SMDSocket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 11.43mm 450mil SMDSocket LongPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-24_W11.43mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-24_W11.43mm_SMDSocket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

