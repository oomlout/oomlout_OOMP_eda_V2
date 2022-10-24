
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_ACP_CA9-V10_Vertical_Hole"
    hexID = "FZKPPOTENTIOMETERACPCA9V1VERTICALHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_ACP_CA9-V10_Vertical_Hole', 'description': 'Potentiometer, vertical, shaft hole, ACP CA9-V10, http://www.acptechnologies.com/wp-content/uploads/2017/05/02-ACP-CA9-CE9.pdf', 'tags': 'Potentiometer vertical hole ACP CA9-V10', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_ACP_CA9-V10_Vertical_Hole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_ACP_CA9-V10_Vertical_Hole')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

