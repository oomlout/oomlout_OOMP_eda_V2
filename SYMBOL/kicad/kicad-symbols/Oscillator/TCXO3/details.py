
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "TCXO3"
    hexID = "SZKOCSTCXO3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'TCXO3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.hcelectronics.cz/PDF/TCXO3_A.pdf', 'kicadSymbolki_keywords': 'Temperature compensated crystal oscillator', 'kicadSymbolki_description': 'Temperature compensated crystal oscillator'}])
    newPart['name'].append('Oscillator : TCXO3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

