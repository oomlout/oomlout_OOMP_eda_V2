
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny13A-SS"
    hexID = "SZKMCUMCHIPATTINYATTINY13ASS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny13V-10SS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny13A-SS', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8126.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 1kB Flash, 64B SRAM, 64B EEPROM, debugWIRE, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny13A-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

