
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Alps_RK09Y11_Single_Horizontal"
    hexID = "FZKPPOTENTIOMETERALPSRK9Y11SINGLEHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Alps_RK09Y11_Single_Horizontal', 'description': 'Potentiometer, horizontal, Long Life, Alps RK09Y11 Single, https://tech.alpsalpine.com/prod/e/pdf/potentiometer/rotarypotentiometers/rk09y11/rk09y11.pdf', 'tags': 'Potentiometer horizontal Alps RK09Y11 Single', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Alps_RK09Y11_Single_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Alps_RK09Y11_Single_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

