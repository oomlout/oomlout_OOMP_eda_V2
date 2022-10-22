
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "VS-6ESU06"
    hexID = "SZKDIODEVS6ESU6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'VS-6ESU06', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-277A', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/94987/vs-6esu06hm3.pdf', 'kicadSymbolki_keywords': 'diode fred', 'kicadSymbolki_description': '600V 6.0A Ultrafast Rectifier, TO-277A', 'kicadSymbolki_fp_filters': 'TO?277A*'}])
    newPart['name'].append('VS-6ESU06')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

