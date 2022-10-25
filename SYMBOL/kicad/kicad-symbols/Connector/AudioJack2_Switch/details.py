
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AudioJack2_Switch"
    hexID = "SZKCNAUDIOJ2SWITCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AudioJack2_Switch', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'audio jack receptacle mono headphones phone TS connector', 'kicadSymbolki_description': 'Audio Jack, 2 Poles (Mono / TS), Switched Pole (Normalling)', 'kicadSymbolki_fp_filters': 'Jack*'}])
    newPart['name'].append('Connector : AudioJack2_Switch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

