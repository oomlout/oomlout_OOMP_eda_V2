
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega8E5-M4"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA8E5M4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega8E5-M4', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8153-8-and-16-bit-AVR-Microcontroller-XMEGA-E-ATxmega8E5-ATxmega16E5-ATxmega32E5_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 8kB Flash, 2kB Boot, 1kB SRAM, 512B EEPROM, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega8E5-M4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

