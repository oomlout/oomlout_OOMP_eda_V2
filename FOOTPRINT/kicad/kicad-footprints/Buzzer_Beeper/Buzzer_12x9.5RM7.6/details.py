
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Buzzer_12x9.5RM7.6"
    hexID = "FZKBZBUZZER12X95RM76"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Buzzer_12x9.5RM7.6', 'description': 'Generic Buzzer, D12mm height 9.5mm with RM7.6mm', 'tags': 'buzzer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Buzzer_12x9.5RM7.6.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Buzzer_12x9.5RM7.6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

