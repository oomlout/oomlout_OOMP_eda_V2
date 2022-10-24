
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Runtron_RM-065_Vertical"
    hexID = "FZKPPOTENTIOMETERRUNTRONRM65VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Runtron_RM-065_Vertical', 'description': 'Potentiometer, vertical, Trimmer, RM-065 https://components101.com/sites/default/files/component_datasheet/Preset%20Potentiometer%20%28Trimpot%29.pdf', 'tags': 'Potentiometer Trimmer RM-065', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Runtron_RM-065_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Runtron_RM-065_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

