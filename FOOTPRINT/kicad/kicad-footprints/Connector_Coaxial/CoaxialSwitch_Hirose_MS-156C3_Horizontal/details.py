
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "CoaxialSwitch_Hirose_MS-156C3_Horizontal"
    hexID = "FZKCNCOACOAXIALSWITCHHIROSEMS156C3HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CoaxialSwitch_Hirose_MS-156C3_Horizontal', 'description': 'Subminiature Coaxial Switch 1.35mm High, DC to 11GHz', 'tags': 'Switch Coaxial RF', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/CoaxialSwitch_Hirose_MS-156C3_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : CoaxialSwitch_Hirose_MS-156C3_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

