
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "MagneticBuzzer_PUI_AT-0927-TT-6-R"
    hexID = "FZKBZMAGNETICBUZZERPUIAT927TT6R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MagneticBuzzer_PUI_AT-0927-TT-6-R', 'description': 'Buzzer Magnetic 9mm AT-0927-TT-6-R, http://www.puiaudio.com/pdf/AT-0927-TT-6-R.pdf', 'tags': 'Buzzer Magnetic 9mm AT-0927-TT-6-R', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/MagneticBuzzer_PUI_AT-0927-TT-6-R.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : MagneticBuzzer_PUI_AT-0927-TT-6-R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

