
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny3226-S"
    hexID = "SZKMCUMCHIPATTINYATTINY3226S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny406-S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny3226-S', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny3224-3226-3227-Data-Sheet-DS40002345A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 32kB Flash, 3kB SRAM, 256B EEPROM, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny3226-S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

