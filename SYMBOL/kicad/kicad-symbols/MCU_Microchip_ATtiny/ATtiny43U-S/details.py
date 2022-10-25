
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny43U-S"
    hexID = "SZKMCUMCHIPATTINYATTINY43US"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny43U-S', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8048.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR Battery Boost', 'kicadSymbolki_description': '8MHz, 4kB Flash, 256B SRAM, 64B EEPROM, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny43U-S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

