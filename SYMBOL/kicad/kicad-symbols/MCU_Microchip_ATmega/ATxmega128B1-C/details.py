
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega128B1-C"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA128B1C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega64B1-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega128B1-C', 'kicadSymbolFootprint': 'Package_BGA:VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8330-8-and-16-bit-AVR-Microcontroller-XMEGA-B-ATxmega64B1-ATxmega128B1_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 128kB Flash, 8kB Boot, 8kB SRAM, 2kB EEPROM, JTAG, USB, LCD, VFBGA-100', 'kicadSymbolki_fp_filters': 'VFBGA*7.0x7.0mm*Layout10x10*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega128B1-C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

