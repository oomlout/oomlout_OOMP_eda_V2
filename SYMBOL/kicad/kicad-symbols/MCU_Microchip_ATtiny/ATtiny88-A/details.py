
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny88-A"
    hexID = "SZKMCUMCHIPATTINYATTINY88A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny48-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny88-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8008.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '12MHz, 8kB Flash, 512B SRAM, 64B EEPROM, TQFP-32', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny88-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

