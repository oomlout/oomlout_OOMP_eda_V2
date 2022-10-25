
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_ACP_CA6-VSMD_Vertical_Hole"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERACPCA6VSMVERTICALHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_ACP_CA6-VSMD_Vertical_Hole', 'description': 'Potentiometer, vertical, shaft hole, ACP CA6-VSMD, http://www.acptechnologies.com/wp-content/uploads/2017/06/01-ACP-CA6.pdf', 'tags': 'Potentiometer vertical hole ACP CA6-VSMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_ACP_CA6-VSMD_Vertical_Hole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_ACP_CA6-VSMD_Vertical_Hole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

