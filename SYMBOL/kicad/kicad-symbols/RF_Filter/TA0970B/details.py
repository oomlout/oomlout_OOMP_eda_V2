
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "TA0970B"
    hexID = "SZKRFFILTA97B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'TA0970B', 'kicadSymbolFootprint': 'Filter:Filter_SAW-6_3.8x3.8mm', 'kicadSymbolDatasheet': 'https://www.golledge.com/media/3785/mp08167.pdf', 'kicadSymbolki_keywords': 'SAW Filter 1090 bandpass MP08167', 'kicadSymbolki_description': 'Bandpass Filter, 1090MHz, SAW filter 6-pin', 'kicadSymbolki_fp_filters': 'Filter*SAW*3.8x3.8mm*'}])
    newPart['name'].append('RF_Filter : TA0970B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

