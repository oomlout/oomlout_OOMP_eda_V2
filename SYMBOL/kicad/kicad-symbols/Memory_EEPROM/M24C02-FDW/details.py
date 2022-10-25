
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "M24C02-FDW"
    hexID = "SZKMEMORYEEPROMM24C2FDW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'M24C02-WDW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M24C02-FDW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/b0/d8/50/40/5a/85/49/6f/DM00071904.pdf/files/DM00071904.pdf/jcr:content/translations/en.DM00071904.pdf', 'kicadSymbolki_keywords': 'Nonvolatile Non-Volatile Memory ROM ST', 'kicadSymbolki_description': '2Kb (256x8) I2C Serial EEPROM, 1.6-5.5V, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_EEPROM : M24C02-FDW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

