
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Laird_Technologies_BMI-S-230-F_50.8x38.1mm"
    hexID = "FZKRFSLAIRDTECHNOLOGIESBMIS23F58X381"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Laird_Technologies_BMI-S-230-F_50.8x38.1mm', 'description': 'Laird Technologies BMI-S-230-F Shielding Cabinet Two Piece SMD 50.8x38.1mm', 'tags': 'Shielding Cabinet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Laird_Technologies_BMI-S-230-F_50.8x38.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Shielding : Laird_Technologies_BMI-S-230-F_50.8x38.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

