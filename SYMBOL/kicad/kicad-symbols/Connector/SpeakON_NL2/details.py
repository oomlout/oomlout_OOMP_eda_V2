
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "SpeakON_NL2"
    hexID = "SZKCNSPEAKONNL2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SpeakON_NL2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.neutrik.com/en/speakon/', 'kicadSymbolki_keywords': 'speakon connector', 'kicadSymbolki_description': 'speakON Connector, Male or Female, NL2', 'kicadSymbolki_fp_filters': 'Jack*speakON*'}])
    newPart['name'].append('Connector : SpeakON_NL2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

