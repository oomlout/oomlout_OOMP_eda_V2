
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Piher_PT-15-V02_Vertical_Hole"
    hexID = "FZKPPOTENTIOMETERPIHERPT15V2VERTICALHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Piher_PT-15-V02_Vertical_Hole', 'description': 'Potentiometer, vertical, shaft hole, Piher PT-15-V02, http://www.piher-nacesa.com/pdf/14-PT15v03.pdf', 'tags': 'Potentiometer vertical hole Piher PT-15-V02', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Piher_PT-15-V02_Vertical_Hole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Piher_PT-15-V02_Vertical_Hole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

