
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "LFCN-9170"
    hexID = "SZKRFFILLFCN917"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LFCN-113', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'LFCN-9170', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-4', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/LFCN-9170+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits low pass filter', 'kicadSymbolki_description': '9170MHz 50 Ohm Passive Low Pass Filter, FV1206-4', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?4*'}])
    newPart['name'].append('LFCN-9170')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

