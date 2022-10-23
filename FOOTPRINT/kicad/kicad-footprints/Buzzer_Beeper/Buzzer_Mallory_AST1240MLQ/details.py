
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Buzzer_Mallory_AST1240MLQ"
    hexID = "FZKBZBUZZERMALLORYAST124MLQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Buzzer_Mallory_AST1240MLQ', 'description': 'Mallory low-profile piezo buzzer, https://www.mspindy.com/specifications/AST12140MLQ.pdf', 'tags': 'piezo buzzer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Buzzer_Mallory_AST1240MLQ.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Buzzer_Mallory_AST1240MLQ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

