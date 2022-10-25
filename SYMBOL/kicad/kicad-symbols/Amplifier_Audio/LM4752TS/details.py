
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4752TS"
    hexID = "SZKAMPLIFIERAUDIOLM4752TS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4752TS', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin4', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4752.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': 'Stereo 11W Audio Power Amplifier, TO-263-7', 'kicadSymbolki_fp_filters': 'TO?263*TabPin4*'}])
    newPart['name'].append('Amplifier_Audio : LM4752TS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

