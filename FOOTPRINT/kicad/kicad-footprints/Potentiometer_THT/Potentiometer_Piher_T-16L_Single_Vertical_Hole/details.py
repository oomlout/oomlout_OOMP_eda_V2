
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Piher_T-16L_Single_Vertical_Hole"
    hexID = "FZKPPOTENTIOMETERPIHERT16LSINGLEVERTICALHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Piher_T-16L_Single_Vertical_Hole', 'description': 'Potentiometer, vertical, shaft hole, Piher T-16L Single, http://www.piher-nacesa.com/pdf/22-T16v03.pdf', 'tags': 'Potentiometer vertical hole Piher T-16L Single', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Piher_T-16L_Single_Vertical_Hole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Piher_T-16L_Single_Vertical_Hole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

