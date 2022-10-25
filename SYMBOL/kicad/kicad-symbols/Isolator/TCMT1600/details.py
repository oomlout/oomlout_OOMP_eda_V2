
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TCMT1600"
    hexID = "SZKISOLATORTCMT16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP290', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCMT1600', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83512/tcmt1600.pdf', 'kicadSymbolki_keywords': 'NPN AC DC Phototransistor Optocoupler', 'kicadSymbolki_description': 'AC/DC Phototransistor Optocoupler, Vce 70V, CTR 80-300%, SOP4', 'kicadSymbolki_fp_filters': 'SOP*4*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TCMT1600')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

