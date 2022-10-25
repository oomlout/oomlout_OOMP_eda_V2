
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4766"
    hexID = "SZKAMPLIFIERAUDIOLM4766"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4766', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4766.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': 'Overture Audio Power Amplifier Series Dual 40W Audio Power Amplifier with Mute, TO-220-15', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : LM4766')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

