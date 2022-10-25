
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "CAT24M01X"
    hexID = "SZKMEMORYEEPROMCAT24M1X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT24M01X', 'kicadSymbolFootprint': 'Package_SO:SOIC-8W_5.3x5.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/CAT24M01-D.PDF', 'kicadSymbolki_keywords': 'EEPROM 1Mb I2C', 'kicadSymbolki_description': '1 Mb I2C CMOS Serial EEPROM, SOIC-8W', 'kicadSymbolki_fp_filters': 'SOIC*5.3x5.3mm*P1.27mm*'}])
    newPart['name'].append('Memory_EEPROM : CAT24M01X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

