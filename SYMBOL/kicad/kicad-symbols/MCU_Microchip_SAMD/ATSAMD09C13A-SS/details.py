
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD09C13A-SS"
    hexID = "SZKMCUMCHIPSAMDATSAMD9C13ASS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD09C13A-SS', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42414-SAM-D09_Datasheet.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 48MHz, 8KB Flash, 4KB RAM, 2.4-3.6V, 12 GPIO, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD09C13A-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

