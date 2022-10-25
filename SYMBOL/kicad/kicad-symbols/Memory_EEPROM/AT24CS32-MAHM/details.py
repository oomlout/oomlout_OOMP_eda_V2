
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "AT24CS32-MAHM"
    hexID = "SZKMEMORYEEPROMAT24CS32MAHM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT24CS01-MAHM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT24CS32-MAHM', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8869-SEEPROM-AT24CS32-Datasheet.pdf', 'kicadSymbolki_keywords': 'I2C Serial EEPROM Nonvolatile Memory', 'kicadSymbolki_description': 'I2C Serial EEPROM, 32Kb (4096x8) with Unique Serial Number, UDFN8', 'kicadSymbolki_fp_filters': 'DFN*3x2mm*P0.5mm*'}])
    newPart['name'].append('Memory_EEPROM : AT24CS32-MAHM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

