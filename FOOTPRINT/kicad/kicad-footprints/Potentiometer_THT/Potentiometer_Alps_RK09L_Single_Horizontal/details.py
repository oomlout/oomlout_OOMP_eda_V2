
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Alps_RK09L_Single_Horizontal"
    hexID = "FZKPPOTENTIOMETERALPSRK9LSINGLEHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Alps_RK09L_Single_Horizontal', 'description': '1120A5F 1120036 1120A0Z 112003S Potentiometer, horizontal, Alps RK09L Single, https://tech.alpsalpine.com/prod/e/pdf/potentiometer/rotarypotentiometers/rk09l/rk09l.pdf', 'tags': 'Potentiometer horizontal Alps RK09L Single', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Alps_RK09L_Single_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Alps_RK09L_Single_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

