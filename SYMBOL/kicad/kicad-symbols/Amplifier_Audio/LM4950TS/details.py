
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4950TS"
    hexID = "SZKAMPLIFIERAUDIOLM495TS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4950TS', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-9_TabPin5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4950.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': 'Boomer Audio Power Amplifier Series 7.5W Mono-BTL or 3.1W Stereo Audio Power Amplifier, TO-263-9', 'kicadSymbolki_fp_filters': 'TO?263*TabPin5*'}])
    newPart['name'].append('Amplifier_Audio : LM4950TS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

