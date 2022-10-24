
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Laird_Technologies_BMI-S-208-F_39.60x39.60mm"
    hexID = "FZKRFSLAIRDTECHNOLOGIESBMIS28F396X396"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Laird_Technologies_BMI-S-208-F_39.60x39.60mm', 'description': 'Laird Technologies BMI-S-208-F Shielding Cabinet Two Piece SMD 39.60x39.60mm (https://assets.lairdtech.com/home/brandworld/files/Board%20Level%20Shields%20Catalog%20Download.pdf)', 'tags': 'Shielding Cabinet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Laird_Technologies_BMI-S-208-F_39.60x39.60mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Shielding : Laird_Technologies_BMI-S-208-F_39.60x39.60mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

