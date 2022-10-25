
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega640-16C"
    hexID = "SZKMCUMCHIPATMEGAATMEGA6416C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATmega640V-8C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega640-16C', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-100_9.0x9.0mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2549-8-bit-AVR-Microcontroller-ATmega640-1280-1281-2560-2561_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '16MHz, 64kB Flash, 8kB SRAM, 4kB EEPROM, JTAG, TFBGA-100', 'kicadSymbolki_fp_filters': 'TFBGA*9.0x9.0mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega640-16C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

