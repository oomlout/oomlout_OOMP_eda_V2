
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "AT24CS04-STUM"
    hexID = "SZKMEMORYEEPROMAT24CS4STUM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT24CS01-STUM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT24CS04-STUM', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8766-SEEPROM-AT24CS04-08-Datasheet.pdf', 'kicadSymbolki_keywords': 'I2C Serial EEPROM Nonvolatile Memory', 'kicadSymbolki_description': 'I2C Serial EEPROM, 4Kb (512x8) with Unique Serial Number, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Memory_EEPROM : AT24CS04-STUM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

