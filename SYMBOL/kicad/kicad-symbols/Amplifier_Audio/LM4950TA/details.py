
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4950TA"
    hexID = "SZKAMPLIFIERAUDIOLM495TA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4950TA', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4950.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': 'Boomer Audio Power Amplifier Series 7.5W Mono-BTL or 3.1W Stereo Audio Power Amplifier, TO-220-9', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : LM4950TA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

