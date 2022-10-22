
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "SpeakON_NL4"
    hexID = "SZKCNSPEAKONNL4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SpeakON_NL4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.neutrik.com/en/speakon/', 'kicadSymbolki_keywords': 'speakon connector', 'kicadSymbolki_description': 'speakON Connector, Male or Female, NL4', 'kicadSymbolki_fp_filters': 'Jack*speakON*'}])
    newPart['name'].append('SpeakON_NL4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

