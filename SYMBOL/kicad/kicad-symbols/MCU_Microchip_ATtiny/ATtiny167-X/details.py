
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny167-X"
    hexID = "SZKMCUMCHIPATTINYATTINY167X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny87-X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny167-X', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8265-8-bit-AVR-Microcontroller-tinyAVR-ATtiny87-ATtiny167_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR Automotive', 'kicadSymbolki_description': '16MHz, 16kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_ATtiny : ATtiny167-X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

