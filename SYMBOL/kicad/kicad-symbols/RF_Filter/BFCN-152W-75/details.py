
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BFCN-152W-75"
    hexID = "SZKRFFILBFCN152W75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BFCN-152W-75', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-7', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BFCN-1445+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits band pass filter', 'kicadSymbolki_description': '950-1970MHz 75 Ohm Passive Band Pass Filter, FV1206-7', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?7*'}])
    newPart['name'].append('RF_Filter : BFCN-152W-75')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

