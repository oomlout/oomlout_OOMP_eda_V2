
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega128A1U-C"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA128A1UC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega64A1U-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega128A1U-C', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-100_9.0x9.0mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8385-8-and-16-bit-AVR-Microcontroller-ATxmega64A1U-ATxmega128A1U_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 128kB Flash, 8kB Boot, 8kB SRAM, 2kB EEPROM, JTAG, USB, TFBGA-100', 'kicadSymbolki_fp_filters': 'TFBGA*9.0x9.0mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega128A1U-C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

