
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-64_W26.67mm_SMDSocket_LongPads"
    hexID = "FZKDIPDIP64W2667SMSOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-64_W26.67mm_SMDSocket_LongPads', 'description': '64-lead though-hole mounted DIP package, row spacing 26.67 mm (1050 mils), SMDSocket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 26.669999999999998mm 1050mil SMDSocket LongPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-64_W26.67mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-64_W26.67mm_SMDSocket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

