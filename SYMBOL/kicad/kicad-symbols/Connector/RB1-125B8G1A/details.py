
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RB1-125B8G1A"
    hexID = "SZKCNRB1125B8G1A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RB1-125B8G1A', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_UDE_RB1-125B8G1A', 'kicadSymbolDatasheet': 'https://datasheet.lcsc.com/szlcsc/1901091107_UDE-Corp-RB1-125B8G1A_C363353.pdf', 'kicadSymbolki_keywords': 'lan jack transformer ethernet gigabit 10 100 1000 baset', 'kicadSymbolki_description': 'LAN Transformer Jack, RJ45, 10/100/1000 BaseT', 'kicadSymbolki_fp_filters': 'RJ45*UDE*RB1*125B8G1A*'}])
    newPart['name'].append('RB1-125B8G1A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

