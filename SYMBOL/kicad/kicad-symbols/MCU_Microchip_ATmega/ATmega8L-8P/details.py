
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATmega"
    oIndex = "ATmega8L-8P"
    hexID = "SZKMCUMCHIPATMEGAATMEGA8L8P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATmega8L-8P', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-2486-8-bit-avr-microcontroller-atmega8_l_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller MegaAVR', 'kicadSymbolki_description': '8MHz, 8kB Flash, 1kB SRAM, 512B EEPROM, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_ATmega : ATmega8L-8P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

