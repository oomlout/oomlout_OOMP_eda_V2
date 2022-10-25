
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TCMT4106"
    hexID = "SZKISOLATORTCMT416"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCMT4100', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCMT4106', 'kicadSymbolFootprint': 'Package_SO:SOP-16_4.4x10.4mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/84181/tcmt4100.pdf', 'kicadSymbolki_keywords': 'NPN DC opto', 'kicadSymbolki_description': 'Quad Optocoupler, Vce 70V, CTR 100-300%, Viso 3750V (RMS), SOP-16', 'kicadSymbolki_fp_filters': 'SOP*4.4x10.4mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TCMT4106')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

