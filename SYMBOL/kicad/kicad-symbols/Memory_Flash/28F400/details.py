
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "28F400"
    hexID = "SZKMEMORYFLASH28F4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '28F400', 'kicadSymbolFootprint': 'PSOP-44', 'kicadSymbolDatasheet': 'http://download.intel.com/design/archives/flash/docs/29045101.pdf', 'kicadSymbolki_keywords': 'EEPROM FLASH 4MO', 'kicadSymbolki_description': 'PA28F400BX-T/B Flash EEProm 4-MBIT (256Kx16bits, 512Kx8bits) 5V, 12V Prog', 'kicadSymbolki_fp_filters': 'PSOP*'}])
    newPart['name'].append('Memory_Flash : 28F400')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

