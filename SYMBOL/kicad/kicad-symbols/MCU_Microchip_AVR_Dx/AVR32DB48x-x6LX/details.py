
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR32DB48x-x6LX"
    hexID = "SZKMCUMCHIPAVRDXAVR32DB48XX6LX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR32DB48x-x6LX', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.2x4.2mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR32DB28-32-48-DataSheet-DS40002301A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DB', 'kicadSymbolki_description': '24MHz, 32kB Flash, 4kB SRAM, EEPROM with Op Amps and Multi-Voltage I/O, VQFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.4mm*EP4.2x4.2mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR32DB48x-x6LX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

