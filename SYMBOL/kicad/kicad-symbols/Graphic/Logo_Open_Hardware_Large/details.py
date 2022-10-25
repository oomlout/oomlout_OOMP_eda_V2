
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Graphic"
    oIndex = "Logo_Open_Hardware_Large"
    hexID = "SZKGRAPHICLOPENHARDWAREL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': '#LOGO', 'kicadSymbolValue': 'Logo_Open_Hardware_Large', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Logo', 'kicadSymbolki_description': 'Open Hardware logo, large'}])
    newPart['name'].append('Graphic : Logo_Open_Hardware_Large')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

