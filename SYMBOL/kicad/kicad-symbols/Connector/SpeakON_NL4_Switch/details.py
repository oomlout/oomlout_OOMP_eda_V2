
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "SpeakON_NL4_Switch"
    hexID = "SZKCNSPEAKONNL4SWITCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SpeakON_NL4_Switch', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.neutrik.com/en/speakon/', 'kicadSymbolki_keywords': 'speakon connector', 'kicadSymbolki_description': 'speakON Connector, Male or Female, NL4, Switched Pins', 'kicadSymbolki_fp_filters': 'Jack*speakON*'}])
    newPart['name'].append('Connector : SpeakON_NL4_Switch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

