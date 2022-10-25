
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATxmega32E5-A"
    hexID = "SZKMCUMCHIPATMEGAATXMEGA32E5A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATxmega8E5-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATxmega32E5-A', 'kicadSymbolFootprint': 'Package_QFP:TQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8153-8-and-16-bit-AVR-Microcontroller-XMEGA-E-ATxmega8E5-ATxmega16E5-ATxmega32E5_Datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8/16bit Microcontroller XMegaAVR', 'kicadSymbolki_description': '32MHz, 32kB Flash, 4kB Boot, 4kB SRAM, 1kB EEPROM, TQFP-32', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATxmega32E5-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

