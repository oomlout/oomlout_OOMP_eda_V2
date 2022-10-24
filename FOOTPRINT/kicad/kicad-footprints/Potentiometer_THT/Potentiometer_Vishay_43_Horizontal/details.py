
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Vishay_43_Horizontal"
    hexID = "FZKPPOTENTIOMETERVISHAY43HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Vishay_43_Horizontal', 'description': 'Potentiometer, horizontal, Vishay 43, http://www.vishay.com/docs/57026/43.pdf', 'tags': 'Potentiometer horizontal Vishay 43', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Vishay_43_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Vishay_43_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

