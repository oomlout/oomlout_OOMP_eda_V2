
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_Earth_Protective_Small"
    hexID = "SZKGRAPHICSYMEARTHPROTECTIVESLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_Earth_Protective_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'graphical symbol earth protective', 'kicadSymbolki_description': 'Protective earth symbol, small'}])
    newPart['name'].append('Graphic : SYM_Earth_Protective_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

