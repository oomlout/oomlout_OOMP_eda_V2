
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-262-3-1EP_Horizontal_TabDown"
    hexID = "FZKSOTTO26231EPHORIZONTALTABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-262-3-1EP_Horizontal_TabDown', 'description': 'TO-262-3, Horizontal, RM 2.54mm, IIPAK, I2PAK, see http://www.onsemi.com/pub/Collateral/EN8586-D.PDF', 'tags': 'TO-262-3 Horizontal RM 2.54mm IIPAK I2PAK', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-262-3-1EP_Horizontal_TabDown.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-262-3-1EP_Horizontal_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

