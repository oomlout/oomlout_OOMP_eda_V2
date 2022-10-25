
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_SAMD"
    oIndex = "ATSAMD09D14A-M"
    hexID = "SZKMCUMCHIPSAMDATSAMD9D14AM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMD09D14A-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42414-SAM-D09_Datasheet.pdf', 'kicadSymbolki_keywords': '32-bit ARM Cortex-M0+ MCU Microcontroller', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 48MHz, 16KB Flash, 4KB RAM, 2.4-3.6V, 22 GPIO, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_Microchip_SAMD : ATSAMD09D14A-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

