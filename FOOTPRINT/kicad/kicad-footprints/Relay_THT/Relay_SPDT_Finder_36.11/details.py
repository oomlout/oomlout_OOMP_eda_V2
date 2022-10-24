
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_Finder_36.11"
    hexID = "FZKRELRELAYSPDTFINDER3611"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_Finder_36.11', 'description': 'FINDER 36.11, SPDT relay, 10A, https://gfinder.findernet.com/public/attachments/36/EN/S36EN.pdf', 'tags': 'spdt relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPDT_Finder_36.11.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_Finder_36.11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

