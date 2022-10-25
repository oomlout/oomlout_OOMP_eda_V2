
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR_Dx"
    oIndex = "AVR32DB28x-xSS"
    hexID = "SZKMCUMCHIPAVRDXAVR32DB28XXSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AVR32DB28x-xSO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AVR32DB28x-xSS', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/AVR32DB28-32-48-DataSheet-DS40002301A.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller AVR-DB', 'kicadSymbolki_description': '24MHz, 32kB Flash, 4kB SRAM, EEPROM with Op Amps and Multi-Voltage I/O, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_AVR_Dx : AVR32DB28x-xSS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

