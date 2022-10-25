
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "DIP_Socket-22_W6.9_W7.62_W10.16_W12.7_W13.5_3M_222-3343-00-0602J"
    hexID = "FZKSODIPSO22W69W762W116W127W1353M222334362J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP_Socket-22_W6.9_W7.62_W10.16_W12.7_W13.5_3M_222-3343-00-0602J', 'description': '3M 22-pin zero insertion force socket, through-hole, row spacing 10.16 mm (400 mils), http://multimedia.3m.com/mws/media/494546O/3mtm-dip-sockets-100-2-54-mm-ts0365.pdf', 'tags': 'THT DIP DIL ZIF 10.16mm 400mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/DIP_Socket-22_W6.9_W7.62_W10.16_W12.7_W13.5_3M_222-3343-00-0602J.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Socket : DIP_Socket-22_W6.9_W7.62_W10.16_W12.7_W13.5_3M_222-3343-00-0602J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

