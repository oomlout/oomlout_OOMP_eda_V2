
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "STK672-040-E"
    hexID = "FZKSIPSTK6724E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'STK672-040-E', 'description': 'SIP-22 (http://www.onsemi.com/pub_link/Collateral/EN5227-D.PDF)', 'tags': 'SIP-22', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/STK672-040-E.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : STK672-040-E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

