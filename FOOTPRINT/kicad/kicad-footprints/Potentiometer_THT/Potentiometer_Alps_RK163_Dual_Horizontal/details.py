
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Alps_RK163_Dual_Horizontal"
    hexID = "FZKPPOTENTIOMETERALPSRK163DUALHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Alps_RK163_Dual_Horizontal', 'description': '12101A2 1210AX9 12A0B85 12A0BKR  Potentiometer, horizontal, Alps RK163 Dual, https://tech.alpsalpine.com/prod/e/pdf/potentiometer/rotarypotentiometers/rk16/rk16.pdf', 'tags': 'Potentiometer horizontal Alps RK163 Dual', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Alps_RK163_Dual_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Alps_RK163_Dual_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

