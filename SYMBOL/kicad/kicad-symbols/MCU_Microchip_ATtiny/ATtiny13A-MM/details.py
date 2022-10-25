
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny13A-MM"
    hexID = "SZKMCUMCHIPATTINYATTINY13A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny13V-10MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny13A-MM', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.75x2.7mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc8126.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 1kB Flash, 64B SRAM, 64B EEPROM, debugWIRE, DFN-10', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny13A-MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

