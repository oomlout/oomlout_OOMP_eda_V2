
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "29F010-TSOP-SP"
    hexID = "SZKMEMORYFLASH29F1TSSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '29F010-TSOP-SP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'EEPROM FLASH 128KO', 'kicadSymbolki_description': 'Flash EEProm 128Ko (TSOP 32 pack.) 5V prog'}])
    newPart['name'].append('Memory_Flash : 29F010-TSOP-SP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

