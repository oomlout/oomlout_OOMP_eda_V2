
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "AT24CS32-SSHM"
    hexID = "SZKMEMORYEEPROMAT24CS32SSHM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT24CS32-SSHM', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8869-SEEPROM-AT24CS32-Datasheet.pdf', 'kicadSymbolki_keywords': 'I2C Serial EEPROM Nonvolatile Memory', 'kicadSymbolki_description': 'I2C Serial EEPROM, 32Kb (4096x8) with Unique Serial Number, SO8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Memory_EEPROM : AT24CS32-SSHM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

