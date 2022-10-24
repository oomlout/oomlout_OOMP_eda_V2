
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "3M_Textool_240-1288-00-0602J_2x20_P2.54mm"
    hexID = "FZKSO3MTEXTOOL24128862J2X2P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': '3M_Textool_240-1288-00-0602J_2x20_P2.54mm', 'description': '3M 40-pin zero insertion force socket, though-hole, row spacing 25.4 mm (1000 mils)', 'tags': 'THT DIP DIL ZIF 25.4mm 1000mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/3M_Textool_240-1288-00-0602J_2x20_P2.54mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Socket : 3M_Textool_240-1288-00-0602J_2x20_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

