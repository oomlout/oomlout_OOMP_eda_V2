
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "MagneticBuzzer_CUI_CMT-8504-100-SMT"
    hexID = "FZKBZMAGNETICBUZZERCUICMT8541S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MagneticBuzzer_CUI_CMT-8504-100-SMT', 'description': 'magnetic transducer buzzer, 5V, SPL of 100 dB at 10 cm, https://www.cuidevices.com/product/resource/pdf/cmt-8504-100-smt-tr.pdf', 'tags': 'CMT 8504', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/MagneticBuzzer_CUI_CMT-8504-100-SMT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : MagneticBuzzer_CUI_CMT-8504-100-SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

