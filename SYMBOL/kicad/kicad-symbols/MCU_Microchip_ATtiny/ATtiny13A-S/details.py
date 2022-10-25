
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny13A-S"
    hexID = "SZKMCUMCHIPATTINYATTINY13AS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny13V-10S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny13A-S', 'kicadSymbolFootprint': 'Package_SO:SOIC-8W_5.3x5.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8126.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 1kB Flash, 64B SRAM, 64B EEPROM, debugWIRE, SOIC-8W', 'kicadSymbolki_fp_filters': 'SOIC*5.3x5.3mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny13A-S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

