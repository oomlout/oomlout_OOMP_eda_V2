
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega256C3-A"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA256C3A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega32C3-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega256C3-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_14x14mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8492-8-and-16-bit-AVR-microcontroller-ATxmega32C3_64C3_128C3_192C3_256C3_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 256kB Flash, 8kB Boot, 16kB SRAM, 4kB EEPROM, JTAG, USB, TQFP-64', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega256C3-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

