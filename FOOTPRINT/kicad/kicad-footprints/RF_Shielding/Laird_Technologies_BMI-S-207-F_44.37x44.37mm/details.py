
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Laird_Technologies_BMI-S-207-F_44.37x44.37mm"
    hexID = "FZKRFSLAIRDTECHNOLOGIESBMIS27F4437X4437"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Laird_Technologies_BMI-S-207-F_44.37x44.37mm', 'description': 'Laird Technologies BMI-S-207-F Shielding Cabinet Two Piece SMD 44.37x44.37mm (https://assets.lairdtech.com/home/brandworld/files/Board%20Level%20Shields%20Catalog%20Download.pdf)', 'tags': 'Shielding Cabinet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Laird_Technologies_BMI-S-207-F_44.37x44.37mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Shielding : Laird_Technologies_BMI-S-207-F_44.37x44.37mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

