
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD10D13A-SS"
    hexID = "SZKMCUMCHIPSAMDATSAMD1D13ASS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD10D13A-SS', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42242-SAM-D10_Datasheet.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 48MHz, 8KB Flash, 4KB RAM, 1.6-3.6V, 18 GPIO, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD10D13A-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

