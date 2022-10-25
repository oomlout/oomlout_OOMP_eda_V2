
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny841-MM"
    hexID = "SZKMCUMCHIPATTINYATTINY841"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny441-MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny841-MM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_3x3mm_P0.45mm_EP1.6x1.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8495-8-bit-AVR-Microcontrollers-ATtiny441-ATtiny841_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '16MHz, 8kB Flash, 512B SRAM, 512B EEPROM, ADC, ACI, debugWIRE, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.45mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny841-MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

