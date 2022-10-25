
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TCMT4606"
    hexID = "SZKISOLATORTCMT466"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP290-4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCMT4606', 'kicadSymbolFootprint': 'Package_SO:SOP-16_4.55x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83512/tcmt1600.pdf', 'kicadSymbolki_keywords': 'NPN AC DC Quad Phototransistor Optocoupler', 'kicadSymbolki_description': 'Quad AC/DC Phototransistor Optocoupler, Vce 70V, CTR 100-300%, SOP16', 'kicadSymbolki_fp_filters': 'SOP*4.55x10.3mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TCMT4606')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

