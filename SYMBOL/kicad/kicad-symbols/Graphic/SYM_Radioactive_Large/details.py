
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_Radioactive_Large"
    hexID = "SZKGRAPHICSYMRADIOACTIVEL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_Radioactive_Large', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'symbol logo radioactive radiation warning heat', 'kicadSymbolki_description': 'Radioactive/radiation warning symbol, large'}])
    newPart['name'].append('Graphic : SYM_Radioactive_Large')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

