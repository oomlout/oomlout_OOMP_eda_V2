
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega32D4-C"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA32D4C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega16D4-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega32D4-C', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8135-8-and-16-bit-AVR-microcontroller-ATxmega16D4-32D4-64D4-128D4_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 32kB Flash, 4kB Boot, 4kB SRAM, 1kB EEPROM, JTAG, VFBGA-49', 'kicadSymbolki_fp_filters': 'VFBGA*5.0x5.0mm*Layout7x7*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega32D4-C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

