
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR"
    oIndex = "AT90PWM1-16S"
    hexID = "SZKMCUMCHIPAVRAT9PWM116S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT90PWM1-16S', 'kicadSymbolFootprint': 'Package_SO:SOIC-24W_7.5x15.4mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc4378.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller LightingAVR PWM', 'kicadSymbolki_description': '16MHz, 8kB Flash, 512B SRAM, 512B EEPROM, SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_AVR : AT90PWM1-16S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

