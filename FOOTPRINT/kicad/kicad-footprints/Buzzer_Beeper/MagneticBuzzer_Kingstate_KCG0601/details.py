
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "MagneticBuzzer_Kingstate_KCG0601"
    hexID = "FZKBZMAGNETICBUZZERKINGSTATEKCG61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MagneticBuzzer_Kingstate_KCG0601', 'description': 'Buzzer, Elektromagnetic Beeper, Summer,', 'tags': 'Kingstate KCG0601 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/MagneticBuzzer_Kingstate_KCG0601.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : MagneticBuzzer_Kingstate_KCG0601')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

