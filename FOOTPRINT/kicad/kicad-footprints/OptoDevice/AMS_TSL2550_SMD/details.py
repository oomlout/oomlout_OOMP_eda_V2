
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "AMS_TSL2550_SMD"
    hexID = "FZKOPAMSTSL255SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMS_TSL2550_SMD', 'description': 'http://ams.com/eng/content/download/250130/975613/142977', 'tags': 'TSL2550 ambient light sensor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/AMS_TSL2550_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : AMS_TSL2550_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

