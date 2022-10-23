
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Indicator_PUI_AI-1440-TWT-24V-2-R"
    hexID = "FZKBZINDICATORPUIAI144TWT24V2R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Indicator_PUI_AI-1440-TWT-24V-2-R', 'description': '14mm Indicator, https://www.puiaudio.com/media/SpecSheet/AI-1440-TWT-24V-2-R.pdf', 'tags': 'piezo buzzer self drive oscillator', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Indicator_PUI_AI-1440-TWT-24V-2-R.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Buzzer_Beeper : Indicator_PUI_AI-1440-TWT-24V-2-R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

