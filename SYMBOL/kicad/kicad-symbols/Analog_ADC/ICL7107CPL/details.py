
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ICL7107CPL"
    hexID = "SZKANALOGADCICL717CPL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ICL7106CPL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICL7107CPL', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'https://www.renesas.com/eu/en/www/doc/datasheet/icl7106-07-07s.pdf', 'kicadSymbolki_keywords': 'LED ADC', 'kicadSymbolki_description': '3 1/2 Digit, LED Display, A/D Converter, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24*'}])
    newPart['name'].append('ICL7107CPL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

