
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "CXO_DIP8"
    hexID = "SZKOCSCXODIP8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'CXO_DIP8', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-8', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/B400/OSZI.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Clock Oscillator, DIP8-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*8*'}])
    newPart['name'].append('Oscillator : CXO_DIP8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

