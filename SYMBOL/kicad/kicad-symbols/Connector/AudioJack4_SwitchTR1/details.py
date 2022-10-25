
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AudioJack4_SwitchTR1"
    hexID = "SZKCNAUDIOJ4SWITCHTR1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AudioJack4_SwitchTR1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'audio jack receptacle stereo headphones phones TRS connector', 'kicadSymbolki_description': 'Audio Jack, 4 Poles (Stereo / TRRS), Switched TR1 Poles (Normalling)', 'kicadSymbolki_fp_filters': 'Jack*'}])
    newPart['name'].append('Connector : AudioJack4_SwitchTR1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

