
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "AT24CS16-XHM"
    hexID = "SZKMEMORYEEPROMAT24CS16XHM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT24CS16-XHM', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8859-SEEPROM-AT24CS16-Datasheet.pdf', 'kicadSymbolki_keywords': 'I2C Serial EEPROM Nonvolatile Memory', 'kicadSymbolki_description': 'I2C Serial EEPROM, 16Kb (2048x8) with Unique Serial Number, TSSOP8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_EEPROM : AT24CS16-XHM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

