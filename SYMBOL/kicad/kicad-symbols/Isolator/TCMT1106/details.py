
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TCMT1106"
    hexID = "SZKISOLATORTCMT116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCMT1100', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCMT1106', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83510/tcmt1100.pdf', 'kicadSymbolki_keywords': 'NPN DC opto', 'kicadSymbolki_description': 'Optocoupler, Vce 70V, CTR 100-300%, Viso 3750V (RMS), SOP-4', 'kicadSymbolki_fp_filters': 'SOP*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TCMT1106')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

