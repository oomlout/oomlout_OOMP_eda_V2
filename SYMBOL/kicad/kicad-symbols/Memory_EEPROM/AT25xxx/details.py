
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "AT25xxx"
    hexID = "SZKMEMORYEEPROMAT25XXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '25LCxxx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT25xxx', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8707-SEEPROM-AT25010B-020B-040B-Datasheet.pdf', 'kicadSymbolki_keywords': 'EEPROM memory SPI serial', 'kicadSymbolki_description': 'Microchip SPI Serial EEPROM, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_EEPROM : AT25xxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

