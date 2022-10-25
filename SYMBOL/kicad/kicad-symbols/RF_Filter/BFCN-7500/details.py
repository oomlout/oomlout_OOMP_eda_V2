
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BFCN-7500"
    hexID = "SZKRFFILBFCN75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BFCN-1860', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BFCN-7500', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-4', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BFCN-7500+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits band pass filter', 'kicadSymbolki_description': '7450-7650MHz 50 Ohm Passive Band Pass Filter, FV1206-4', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?4*'}])
    newPart['name'].append('RF_Filter : BFCN-7500')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

