
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-92-2_Horizontal2"
    hexID = "FZKSOTTO922HORIZONTAL2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-92-2_Horizontal2', 'description': '2-pin TO-92 horizontal, leads molded, narrow, drill 0.75mm (see NXP sot054_po.pdf)', 'tags': 'to-92 sc-43 sc-43a sot54 PA33 temperature sensor diode', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92-2_Horizontal2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-92-2_Horizontal2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

