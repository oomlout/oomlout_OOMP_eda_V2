
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny1614-SS"
    hexID = "SZKMCUMCHIPATTINYATTINY1614SS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny204-SS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny1614-SS', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-data-sheet-40001995A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 16kB Flash, 2kB SRAM, 256B EEPROM, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny1614-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

