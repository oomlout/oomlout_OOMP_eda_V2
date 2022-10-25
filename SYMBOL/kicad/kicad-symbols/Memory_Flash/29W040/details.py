
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "29W040"
    hexID = "SZKMEMORYFLASH29W4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '29W040', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'EEPROM FLASH 512KO', 'kicadSymbolki_description': 'Flash EEProm 512PP (TSOP 32) 3,3V'}])
    newPart['name'].append('Memory_Flash : 29W040')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

