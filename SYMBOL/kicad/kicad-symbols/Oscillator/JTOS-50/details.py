
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "JTOS-50"
    hexID = "SZKOCSJTOS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'JTOS-50', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_BK377_LandPatternPL-005', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/JTOS-50+.pdf', 'kicadSymbolki_keywords': 'VCXO', 'kicadSymbolki_description': 'Voltage Controlled Oscillator, 25 to 47 MHz, Mini-Circuits BK377', 'kicadSymbolki_fp_filters': 'Mini?Circuits*BK377*'}])
    newPart['name'].append('Oscillator : JTOS-50')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

