
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD10D14A-U"
    hexID = "SZKMCUMCHIPSAMDATSAMD1D14AU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD10D14A-U', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-20_1.934x2.434mm_Layout4x5_P0.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42242-SAM-D10_Datasheet.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 48MHz, 16KB Flash, 4KB RAM, 1.6-3.6V, 18 GPIO, WLCSP-20', 'kicadSymbolki_fp_filters': 'WLCSP*1.934x2.434mm*Layout4x5*P0.4mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD10D14A-U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

