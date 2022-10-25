
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR128DA32x-xRXB"
    hexID = "SZKMCUMCHIPAVRDXAVR128DA32XXRXB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR32DA32x-xRXB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR128DA32x-xRXB', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR128DA28-32-48-64-DataSheet-DS40002183B.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DA', 'kicadSymbolki_description': '24MHz, 128kB Flash, 16kB SRAM, EEPROM with Touch Sensing, VQFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*EP3.1x3.1mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR128DA32x-xRXB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

