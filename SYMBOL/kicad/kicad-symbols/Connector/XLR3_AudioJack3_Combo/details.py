
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "XLR3_AudioJack3_Combo"
    hexID = "SZKCNXLR3AUDIOJ3COMBO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'XLR3_AudioJack3_Combo', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'xlr connector', 'kicadSymbolki_description': 'XLR (Male or Female) and Audio Jack (Stereo / TRS) Combo Connector, Discrete Ground Pin', 'kicadSymbolki_fp_filters': 'Jack*XLR*6.35mm*'}])
    newPart['name'].append('Connector : XLR3_AudioJack3_Combo')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

