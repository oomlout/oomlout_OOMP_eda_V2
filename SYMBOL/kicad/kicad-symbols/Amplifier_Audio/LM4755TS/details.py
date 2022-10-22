
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4755TS"
    hexID = "SZKAMPLIFIERAUDIOLM4755TS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4755TS', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-9_TabPin5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4755.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': 'Stereo 11W Audio Power Amplifier with Mute, TO-263-9', 'kicadSymbolki_fp_filters': 'TO?263*TabPin5*'}])
    newPart['name'].append('LM4755TS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

