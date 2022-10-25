
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "SYM_Radioactive_Radiation_Small"
    hexID = "SZKGRAPHICSYMRADIOACTIVERADIATIONSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#SYM', 'kicadSymbolValue': 'SYM_Radioactive_Radiation_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'symbol logo radioactive radiation warning', 'kicadSymbolki_description': 'Radioactive/radiation warning symbol, small'}])
    newPart['name'].append('Graphic : SYM_Radioactive_Radiation_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

