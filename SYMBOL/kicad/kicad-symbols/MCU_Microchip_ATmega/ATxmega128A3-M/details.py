
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega128A3-M"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA128A3M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega64A3-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega128A3-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP7.65x7.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8068-8-and16-bit-AVR-XMEGA-A3-Microcontrollers_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 128kB Flash, 8kB Boot, 8kB SRAM, 2kB EEPROM, JTAG, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega128A3-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

