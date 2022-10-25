
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Vishay_T7-YA_Single_Vertical"
    hexID = "FZKPPOTENTIOMETERVISHAYT7YASINGLEVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Vishay_T7-YA_Single_Vertical', 'description': 'Potentiometer, vertical, Vishay T7-YA Single, http://www.vishay.com/docs/51015/t7.pdf', 'tags': 'Potentiometer vertical Vishay T7-YA Single', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Vishay_T7-YA_Single_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Vishay_T7-YA_Single_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

