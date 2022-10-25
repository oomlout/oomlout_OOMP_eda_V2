
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "TFT680"
    hexID = "SZKOCSTFT68"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CXO_DIP14', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'TFT680', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-14', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/B400/OSZI.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Clock Oscillator, DIP14-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*14*'}])
    newPart['name'].append('Oscillator : TFT680')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

