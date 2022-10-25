
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "DIP_Socket-40_W22.1_W22.86_W25.4_W27.94_W28.7_3M_240-3639-00-0602J"
    hexID = "FZKSODIPSO4W221W2286W254W2794W2873M24363962J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP_Socket-40_W22.1_W22.86_W25.4_W27.94_W28.7_3M_240-3639-00-0602J', 'description': '3M 40-pin zero insertion force socket, through-hole, row spacing 25.4 mm (1000 mils), http://multimedia.3m.com/mws/media/494546O/3mtm-dip-sockets-100-2-54-mm-ts0365.pdf', 'tags': 'THT DIP DIL ZIF 25.4mm 1000mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/DIP_Socket-40_W22.1_W22.86_W25.4_W27.94_W28.7_3M_240-3639-00-0602J.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Socket : DIP_Socket-40_W22.1_W22.86_W25.4_W27.94_W28.7_3M_240-3639-00-0602J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

