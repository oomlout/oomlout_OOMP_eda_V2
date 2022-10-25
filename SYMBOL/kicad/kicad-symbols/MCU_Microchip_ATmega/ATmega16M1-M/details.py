
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega16M1-M"
    hexID = "SZKMCUMCHIPATMEGAATMEGA16M1M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega16M1-M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_7x7mm_P0.65mm_EP4.65x4.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8209-8-bit%20AVR%20ATmega16M1-32M1-64M1_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '16MHz, 16kB Flash, 1kB SRAM, 512B EEPROM, CAN, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega16M1-M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

