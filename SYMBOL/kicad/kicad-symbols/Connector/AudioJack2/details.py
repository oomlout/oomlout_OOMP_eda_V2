
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AudioJack2"
    hexID = "SZKCNAUDIOJ2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AudioJack2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'audio jack receptacle mono phone headphone TS connector', 'kicadSymbolki_description': 'Audio Jack, 2 Poles (Mono / TS)', 'kicadSymbolki_fp_filters': 'Jack*'}])
    newPart['name'].append('Connector : AudioJack2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

