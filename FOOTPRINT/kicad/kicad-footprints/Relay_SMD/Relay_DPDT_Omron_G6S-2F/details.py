
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_DPDT_Omron_G6S-2F"
    hexID = "FZKRELAYSMRELAYDPDTOMRONG6S2F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Omron_G6S-2F', 'description': 'Relay Omron G6S-2F, see http://omronfs.omron.com/en_US/ecb/products/pdf/en-g6s.pdf', 'tags': 'Relay Omron G6S-2F', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_DPDT_Omron_G6S-2F.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Relay_SMD : Relay_DPDT_Omron_G6S-2F')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

