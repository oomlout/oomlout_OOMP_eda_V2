
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny28L-4M"
    hexID = "SZKMCUMCHIPATTINYATTINY28L4M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny28V-1M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny28L-4M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc1062.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR IR', 'kicadSymbolki_description': '4MHz, 2kB Flash, No SRAM, No EEPROM, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny28L-4M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

