
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Alps_RK097_Dual_Horizontal_Switch"
    hexID = "FZKPPOTENTIOMETERALPSRK97DUALHORIZONTALSWITCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Alps_RK097_Dual_Horizontal_Switch', 'description': '1221-5R1211, Dual Pot, Horizontal, Switch, Alps RK097 Dual, https://tech.alpsalpine.com/prod/e/pdf/potentiometer/rotarypotentiometers/rk097/rk097.pdf', 'tags': 'Potentiometer horizontal Alps RK097 Dual Switch', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Alps_RK097_Dual_Horizontal_Switch.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Alps_RK097_Dual_Horizontal_Switch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

