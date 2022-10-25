
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "TA0232A"
    hexID = "SZKRFFILTA232A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'TA0232A', 'kicadSymbolFootprint': 'Filter:Filter_SAW-8_3.8x3.8mm', 'kicadSymbolDatasheet': 'https://www.golledge.com/media/1831/ma05497.pdf', 'kicadSymbolki_keywords': 'SAW Filter 1090 bandpass', 'kicadSymbolki_description': 'Bandpass Filter, 1090MHz, SAW filter 8-pin', 'kicadSymbolki_fp_filters': 'Filter*SAW*3.8x3.8mm*'}])
    newPart['name'].append('RF_Filter : TA0232A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

