
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BFCN-1560"
    hexID = "SZKRFFILBFCN156"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BFCN-1560', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-1', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BFCN-1560+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits band pass filter', 'kicadSymbolki_description': '1500-1620MHz 50 Ohm Passive Band Pass Filter, FV1206-1', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?1*'}])
    newPart['name'].append('RF_Filter : BFCN-1560')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

