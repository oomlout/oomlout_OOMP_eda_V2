
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "MagneticBuzzer_Kobitone_254-EMB84Q-RO"
    hexID = "FZKBZMAGNETICBUZZERKOBITONE254EMB84QRO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MagneticBuzzer_Kobitone_254-EMB84Q-RO', 'description': 'MagneticBuzzer Kobitone 254-EMB84Q-RO https://www.mouser.es/datasheet/2/209/KT-400385-1171904.pdf', 'tags': 'MagneticBuzzer Kobitone 254-EMB84Q-RO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/MagneticBuzzer_Kobitone_254-EMB84Q-RO.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : MagneticBuzzer_Kobitone_254-EMB84Q-RO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

