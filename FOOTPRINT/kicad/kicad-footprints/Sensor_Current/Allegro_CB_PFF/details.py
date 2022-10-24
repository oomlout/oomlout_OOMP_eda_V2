
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_CB_PFF"
    hexID = "FZKSENCURRENTALLEGROCBPFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_CB_PFF', 'description': 'Allegro MicroSystems, CB-PFF Package (http://www.allegromicro.com/en/Products/Current-Sensor-ICs/Fifty-To-Two-Hundred-Amp-Integrated-Conductor-Sensor-ICs/ACS758.aspx) !PADS 4-5 DO NOT MATCH DATASHEET!', 'tags': 'Allegro CB-PFF', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_CB_PFF.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_CB_PFF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

