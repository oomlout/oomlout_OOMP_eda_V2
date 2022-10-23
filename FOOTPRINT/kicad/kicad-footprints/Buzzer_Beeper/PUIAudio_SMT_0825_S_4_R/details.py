
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "PUIAudio_SMT_0825_S_4_R"
    hexID = "FZKBZPUIAUDIOS825S4R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PUIAudio_SMT_0825_S_4_R', 'description': 'SMD 8540, http://www.puiaudio.com/product-detail.aspx?partnumber=SMT-0825-S-4-R', 'tags': 'SMD 8540', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/PUIAudio_SMT_0825_S_4_R.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : PUIAudio_SMT_0825_S_4_R')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

