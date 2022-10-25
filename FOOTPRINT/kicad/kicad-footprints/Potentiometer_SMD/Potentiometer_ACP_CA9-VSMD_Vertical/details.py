
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_ACP_CA9-VSMD_Vertical"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERACPCA9VSMVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_ACP_CA9-VSMD_Vertical', 'description': 'Potentiometer, vertical, ACP CA9-VSMD, http://www.acptechnologies.com/wp-content/uploads/2017/05/02-ACP-CA9-CE9.pdf', 'tags': 'Potentiometer vertical ACP CA9-VSMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_ACP_CA9-VSMD_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_ACP_CA9-VSMD_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

