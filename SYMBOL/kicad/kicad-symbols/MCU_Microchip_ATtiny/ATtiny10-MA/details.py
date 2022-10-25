
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny10-MA"
    hexID = "SZKMCUMCHIPATTINYATTINY1MA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny4-MA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny10-MA', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8127-AVR-8-bit-Microcontroller-ATtiny4-ATtiny5-ATtiny9-ATtiny10_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '12MHz, 1kB Flash, 32B SRAM, No EEPROM, ADC, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny10-MA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

