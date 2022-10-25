
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-40_W16.51mm_SMDSocket_LongPads"
    hexID = "FZKDIPDIP4W1651SMSOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-40_W16.51mm_SMDSocket_LongPads', 'description': '40-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 16.51mm 650mil SMDSocket LongPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-40_W16.51mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-40_W16.51mm_SMDSocket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

