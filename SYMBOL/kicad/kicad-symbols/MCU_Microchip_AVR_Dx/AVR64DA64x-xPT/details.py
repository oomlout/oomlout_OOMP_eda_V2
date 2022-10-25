
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR64DA64x-xPT"
    hexID = "SZKMCUMCHIPAVRDXAVR64DA64XXPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR64DA64x-xPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR64DA28-32-48-64-Data-Sheet-40002233B.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DA', 'kicadSymbolki_description': '24MHz, 64kB Flash, 8kB SRAM, EEPROM with Touch Sensing, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR64DA64x-xPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

