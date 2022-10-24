
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_ACP_CA14-H2,5_Horizontal"
    hexID = "FZKPPOTENTIOMETERACPCA14H25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_ACP_CA14-H2,5_Horizontal', 'description': 'Potentiometer, horizontal, ACP CA14-H2,5, http://www.acptechnologies.com/wp-content/uploads/2017/10/03-ACP-CA14-CE14.pdf', 'tags': 'Potentiometer horizontal ACP CA14-H2,5', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_ACP_CA14-H2,5_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_ACP_CA14-H2,5_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

