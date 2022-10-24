
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "SIP9_Housing_BigPads"
    hexID = "FZKSIPSIP9HOUSINGBIGPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SIP9_Housing_BigPads', 'description': 'SIP9, large pads', 'tags': 'SIP9', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/SIP9_Housing_BigPads.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : SIP9_Housing_BigPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

