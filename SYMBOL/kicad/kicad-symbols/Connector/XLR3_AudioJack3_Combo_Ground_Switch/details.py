
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "XLR3_AudioJack3_Combo_Ground_Switch"
    hexID = "SZKCNXLR3AUDIOJ3COMBOGROUNDSWITCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'XLR3_AudioJack3_Combo_Ground_Switch', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'xlr connector', 'kicadSymbolki_description': 'XLR (Male or Female) and Audio Jack (Stereo / TRS, Switched Poles (Normalling)) Combo Connector, Discrete Ground Pin', 'kicadSymbolki_fp_filters': 'Jack*XLR*6.35mm*'}])
    newPart['name'].append('XLR3_AudioJack3_Combo_Ground_Switch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

