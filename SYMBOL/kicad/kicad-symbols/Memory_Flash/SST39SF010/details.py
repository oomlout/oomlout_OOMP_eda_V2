
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "SST39SF010"
    hexID = "SZKMEMORYFLASHSST39SF1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SST39SF010', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/25022B.pdf', 'kicadSymbolki_keywords': '128k flash rom', 'kicadSymbolki_description': 'Silicon Storage Technology (SSF) 128k x 8 Flash ROM'}])
    newPart['name'].append('Memory_Flash : SST39SF010')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

