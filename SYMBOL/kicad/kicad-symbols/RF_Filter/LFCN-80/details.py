
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "LFCN-80"
    hexID = "SZKRFFILLFCN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'LFCN-80', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/LFCN-80+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits low pass filter', 'kicadSymbolki_description': '80MHz 50 Ohm Passive Low Pass Filter, FV1206', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206*'}])
    newPart['name'].append('RF_Filter : LFCN-80')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

