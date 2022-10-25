
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-14_W8.89mm_SMDSocket_LongPads"
    hexID = "FZKDIPDIP14W889SMSOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-14_W8.89mm_SMDSocket_LongPads', 'description': '14-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 8.89mm 350mil SMDSocket LongPads', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-14_W8.89mm_SMDSocket.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-14_W8.89mm_SMDSocket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

