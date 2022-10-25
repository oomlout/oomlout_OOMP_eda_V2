
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "RLP-30"
    hexID = "SZKRFFILRLP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RLP-30', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_GP1212_LandPatternPL-176', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/RLP-30+.pdf', 'kicadSymbolki_keywords': 'Low Pass Filter', 'kicadSymbolki_description': 'Low Pass Filter, DC to 30 MHz, 50 Ohm, Mini-Circuits GP1212', 'kicadSymbolki_fp_filters': 'Mini?Circuits*GP1212*'}])
    newPart['name'].append('RF_Filter : RLP-30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

