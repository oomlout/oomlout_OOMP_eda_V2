
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4990ITL"
    hexID = "SZKAMPLIFIERAUDIOLM499ITL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4990ITL', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4990.pdf', 'kicadSymbolki_keywords': 'audio amplifier class d', 'kicadSymbolki_description': 'Boomer 2 Watt Audio Power Amplifier with Selectable Shutdown Logic Level, DSBGA-9', 'kicadSymbolki_fp_filters': '*DSBGA*1.4715x1.4715mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : LM4990ITL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

