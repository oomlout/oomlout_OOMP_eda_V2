
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Alpha_RD902F-40-00D_Dual_Vertical_CircularHoles"
    hexID = "FZKPPOTENTIOMETERALPHARD92F4DDUALVERTICALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Alpha_RD902F-40-00D_Dual_Vertical_CircularHoles', 'description': 'Potentiometer, vertical, 9mm, dual, http://www.taiwanalpha.com.tw/downloads?target=products&id=113', 'tags': 'potentiometer vertical 9mm dual', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Alpha_RD902F-40-00D_Dual_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Alpha_RD902F-40-00D_Dual_Vertical_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

