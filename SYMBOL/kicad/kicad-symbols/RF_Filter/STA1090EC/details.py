
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "STA1090EC"
    hexID = "SZKRFFILSTA19EC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TA0970B', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'STA1090EC', 'kicadSymbolFootprint': 'Filter:Filter_SAW-6_3.8x3.8mm', 'kicadSymbolDatasheet': 'https://www.golledge.com/media/3785/mp08167.pdf', 'kicadSymbolki_keywords': 'SAW Filter 1090 bandpass', 'kicadSymbolki_description': 'Bandpass Filter, 1090MHz, SAW filter 6-pin', 'kicadSymbolki_fp_filters': 'Filter*SAW*3.8x3.8mm*'}])
    newPart['name'].append('STA1090EC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

