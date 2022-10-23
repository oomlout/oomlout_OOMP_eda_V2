
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BFCN-1900"
    hexID = "SZKRFFILBFCN19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BFCN-1900', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-5', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BFCN-1900+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits band pass filter', 'kicadSymbolki_description': '1893-1920MHz 50 Ohm Passive Band Pass Filter, FV1206-5', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?5*'}])
    newPart['name'].append('BFCN-1900')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

