
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR"
    oIndex = "AT90USB1287-A"
    hexID = "SZKMCUMCHIPAVRAT9U1287A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT90USB646-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT90USB1287-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_14x14mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc7593.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller USB', 'kicadSymbolki_description': '16MHz, 128kB Flash, 8kB SRAM, 4kB EEPROM, USB 2.0 OTG, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_AVR : AT90USB1287-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

