
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "LFCN-2250"
    hexID = "SZKRFFILLFCN225"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LFCN-80', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'LFCN-2250', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/LFCN-2250+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits low pass filter', 'kicadSymbolki_description': '2200MHz 50 Ohm Passive Low Pass Filter, FV1206', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206*'}])
    newPart['name'].append('LFCN-2250')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

