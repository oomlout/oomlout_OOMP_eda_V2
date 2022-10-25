
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ASCO"
    hexID = "SZKOCSASCO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'ASCO', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Abracon_ASCO-4Pin_1.6x1.2mm', 'kicadSymbolDatasheet': 'https://abracon.com/Oscillators/ASCO.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Clock Oscillator, Abracon ASCO', 'kicadSymbolki_fp_filters': 'Oscillator*Abracon*ASCO*1.6x1.2mm*'}])
    newPart['name'].append('Oscillator : ASCO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

