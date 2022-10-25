
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR64DB48x-xPT"
    hexID = "SZKMCUMCHIPAVRDXAVR64DB48XXPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR32DB48x-xPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR64DB48x-xPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR64DB28-32-48-64-DataSheet-DS40002300A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DB', 'kicadSymbolki_description': '24MHz, 64kB Flash, 8kB SRAM, EEPROM with Op Amps and Multi-Voltage I/O, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR64DB48x-xPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

