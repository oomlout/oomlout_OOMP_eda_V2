
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega32C4-M"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA32C4M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega16C4-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega32C4-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8493-8-and-32-bit-AVR-XMEGA-Microcontrollers-ATxmega16C4-ATxmega32C4_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 32kB Flash, 4kB Boot, 4kB SRAM, 1kB EEPROM, JTAG, QFN-44', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega32C4-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

