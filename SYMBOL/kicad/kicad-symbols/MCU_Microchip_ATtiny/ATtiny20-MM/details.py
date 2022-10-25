
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny20-MM"
    hexID = "SZKMCUMCHIPATTINYATTINY2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny20-MM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_3x3mm_P0.45mm_EP1.6x1.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-8235-8-bit-avr-microcontroller-attiny20_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '12MHz, 2kB Flash, 128B SRAM, No EEPROM, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.45mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny20-MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

