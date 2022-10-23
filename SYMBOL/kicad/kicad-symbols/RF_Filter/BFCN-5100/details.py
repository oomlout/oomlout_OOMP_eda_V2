
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BFCN-5100"
    hexID = "SZKRFFILBFCN51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BFCN-5100', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-6', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BFCN-5100+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits band pass filter', 'kicadSymbolki_description': '3100-7100MHz 50 Ohm Passive Band Pass Filter, FV1206-6', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?6*'}])
    newPart['name'].append('BFCN-5100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

