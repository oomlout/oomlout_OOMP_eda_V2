
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "CAT250xxx"
    hexID = "SZKMEMORYEEPROMCAT25XXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '25LCxxx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT250xxx', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/PowerSolutions/product.do?id=CAT25040', 'kicadSymbolki_keywords': 'EEPROM memory SPI serial', 'kicadSymbolki_description': 'ON Semiconductor SPI Serial EEPROM, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_EEPROM : CAT250xxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

