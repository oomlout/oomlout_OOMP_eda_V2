
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM2876"
    hexID = "SZKAMPLIFIERAUDIOLM2876"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2876', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-11_P3.4x5.08mm_StaggerOdd_Lead4.85mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2876.pdf', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': 'Overture Audio Power Amplifier Series High-Performance 40W Audio Power Amplifier w/Mute, TO-220-11', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : LM2876')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

