
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-22_W10.16mm_Socket_LongPads"
    hexID = "FZKDIPDIP22W116SOL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-22_W10.16mm_Socket_LongPads', 'description': '22-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils), Socket, LongPads', 'tags': 'THT DIP DIL PDIP 2.54mm 10.16mm 400mil Socket LongPads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-22_W10.16mm_Socket.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-22_W10.16mm_Socket_LongPads')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

