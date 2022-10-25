
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "OH300"
    hexID = "SZKOCSOH3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'OH300', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_OCXO_ConnorWinfield_OH300', 'kicadSymbolDatasheet': 'http://www.conwin.com/datasheets/cx/cx282.pdf', 'kicadSymbolki_keywords': 'OCXO', 'kicadSymbolki_description': '100MHz Sinewave output OCXO, low phase-noise, high stability, Connor-Winfield OH300', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*OH300*'}])
    newPart['name'].append('Oscillator : OH300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

