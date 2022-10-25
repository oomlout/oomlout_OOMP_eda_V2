
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4990LD"
    hexID = "SZKAMPLIFIERAUDIOLM499LD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4990LD', 'kicadSymbolFootprint': 'Package_SON:WSON-10-1EP_4x3mm_P0.5mm_EP2.2x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4990.pdf', 'kicadSymbolki_keywords': 'audio amplifier class d', 'kicadSymbolki_description': 'Boomer 2 Watt Audio Power Amplifier with Selectable Shutdown Logic Level, WSON-10', 'kicadSymbolki_fp_filters': 'WSON*EP*4x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : LM4990LD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

