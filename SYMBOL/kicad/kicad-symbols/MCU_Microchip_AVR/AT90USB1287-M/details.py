
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR"
    oIndex = "AT90USB1287-M"
    hexID = "SZKMCUMCHIPAVRAT9U1287M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT90USB646-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT90USB1287-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP7.5x7.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc7593.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller USB', 'kicadSymbolki_description': '16MHz, 128kB Flash, 8kB SRAM, 4kB EEPROM, USB 2.0 OTG, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_AVR : AT90USB1287-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

