
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_Vishay_TS53YJ_Vertical"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERVISHAYTS53YJVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Vishay_TS53YJ_Vertical', 'description': 'Potentiometer, vertical, Vishay TS53YJ, https://www.vishay.com/docs/51008/ts53.pdf', 'tags': 'Potentiometer vertical Vishay TS53YJ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_Vishay_TS53YJ_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_Vishay_TS53YJ_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

