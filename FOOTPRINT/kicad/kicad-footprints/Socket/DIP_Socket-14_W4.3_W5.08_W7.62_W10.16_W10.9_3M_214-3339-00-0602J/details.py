
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "DIP_Socket-14_W4.3_W5.08_W7.62_W10.16_W10.9_3M_214-3339-00-0602J"
    hexID = "FZKSODIPSO14W43W58W762W116W193M214333962J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP_Socket-14_W4.3_W5.08_W7.62_W10.16_W10.9_3M_214-3339-00-0602J', 'description': '3M 14-pin zero insertion force socket, through-hole, row spacing 7.62 mm (300 mils), http://multimedia.3m.com/mws/media/494546O/3mtm-dip-sockets-100-2-54-mm-ts0365.pdf', 'tags': 'THT DIP DIL ZIF 7.62mm 300mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/DIP_Socket-14_W4.3_W5.08_W7.62_W10.16_W10.9_3M_214-3339-00-0602J.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Socket : DIP_Socket-14_W4.3_W5.08_W7.62_W10.16_W10.9_3M_214-3339-00-0602J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

