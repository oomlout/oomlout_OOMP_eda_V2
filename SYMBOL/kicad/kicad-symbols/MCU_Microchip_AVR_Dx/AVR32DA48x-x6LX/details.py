
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR32DA48x-x6LX"
    hexID = "SZKMCUMCHIPAVRDXAVR32DA48XX6LX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR32DA48x-x6LX', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.2x4.2mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR32DA28-32-48-Data-Sheet-40002228B.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DA', 'kicadSymbolki_description': '24MHz, 32kB Flash, 4kB SRAM, EEPROM with Touch Sensing, VQFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.4mm*EP4.2x4.2mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR32DA48x-x6LX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

