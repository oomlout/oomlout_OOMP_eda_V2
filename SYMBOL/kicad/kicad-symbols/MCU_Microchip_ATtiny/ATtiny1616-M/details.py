
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny1616-M"
    hexID = "SZKMCUMCHIPATTINYATTINY1616M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny406-M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny1616-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny3216_ATtiny1616-data-sheet-40001997B.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '20MHz, 16kB Flash, 2kB SRAM, 256B EEPROM, VQFN-20', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny1616-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

