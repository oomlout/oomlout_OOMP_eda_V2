
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Onion_Omega2S"
    hexID = "FZKMOONIONOMEGA2S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Onion_Omega2S', 'description': 'https://github.com/OnionIoT/Omega2/raw/master/Documents/Omega2S%20Datasheet.pdf', 'tags': 'onion omega module', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Onion_Omega2S.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Module : Onion_Omega2S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

