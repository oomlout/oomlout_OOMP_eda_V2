
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "DIP_Socket-40_W11.9_W12.7_W15.24_W17.78_W18.5_3M_240-1280-00-0602J"
    hexID = "FZKSODIPSO4W119W127W1524W1778W1853M2412862J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP_Socket-40_W11.9_W12.7_W15.24_W17.78_W18.5_3M_240-1280-00-0602J', 'description': '3M 40-pin zero insertion force socket, through-hole, row spacing 15.24 mm (600 mils), http://multimedia.3m.com/mws/media/494546O/3mtm-dip-sockets-100-2-54-mm-ts0365.pdf', 'tags': 'THT DIP DIL ZIF 15.24mm 600mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/DIP_Socket-40_W11.9_W12.7_W15.24_W17.78_W18.5_3M_240-1280-00-0602J.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Socket : DIP_Socket-40_W11.9_W12.7_W15.24_W17.78_W18.5_3M_240-1280-00-0602J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

