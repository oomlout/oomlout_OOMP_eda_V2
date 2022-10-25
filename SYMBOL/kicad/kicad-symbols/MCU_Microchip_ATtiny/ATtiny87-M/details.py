
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny87-M"
    hexID = "SZKMCUMCHIPATTINYATTINY87M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny87-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8265-8-bit-AVR-Microcontroller-tinyAVR-ATtiny87-ATtiny167_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR Automotive', 'kicadSymbolki_description': '16MHz, 8kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny87-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

