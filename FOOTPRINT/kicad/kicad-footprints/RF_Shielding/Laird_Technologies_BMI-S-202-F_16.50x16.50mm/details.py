
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Laird_Technologies_BMI-S-202-F_16.50x16.50mm"
    hexID = "FZKRFSLAIRDTECHNOLOGIESBMIS22F165X165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Laird_Technologies_BMI-S-202-F_16.50x16.50mm', 'description': 'Laird Technologies BMI-S-202-F Shielding Cabinet Two Piece SMD 16.50x16.50mm (https://assets.lairdtech.com/home/brandworld/files/Board%20Level%20Shields%20Catalog%20Download.pdf)', 'tags': 'Shielding Cabinet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Laird_Technologies_BMI-S-202-F_16.50x16.50mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Shielding : Laird_Technologies_BMI-S-202-F_16.50x16.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

