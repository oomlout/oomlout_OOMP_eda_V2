
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Laird_Technologies_97-2003_12.70x13.37mm"
    hexID = "FZKRFSLAIRDTECHNOLOGIES9723127X1337"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Laird_Technologies_97-2003_12.70x13.37mm', 'description': 'Laird Technologies 97-2003 EZ PEEL Shielding Cabinet One Piece SMD 12.70x13.37mm (https://assets.lairdtech.com/home/brandworld/files/Board%20Level%20Shields%20Catalog%20Download.pdf)', 'tags': 'Shielding Cabinet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Laird_Technologies_97-2003_12.70x13.37mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Shielding : Laird_Technologies_97-2003_12.70x13.37mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

