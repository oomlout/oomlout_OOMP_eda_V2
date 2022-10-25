
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "CAT24M01Y"
    hexID = "SZKMEMORYEEPROMCAT24M1Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT24M01Y', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/CAT24M01-D.PDF', 'kicadSymbolki_keywords': 'EEPROM 1Mb I2C', 'kicadSymbolki_description': '1 Mb I2C CMOS Serial EEPROM, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_EEPROM : CAT24M01Y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

