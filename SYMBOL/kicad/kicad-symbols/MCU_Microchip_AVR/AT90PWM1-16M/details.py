
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_AVR"
    oIndex = "AT90PWM1-16M"
    hexID = "SZKMCUMCHIPAVRAT9PWM116M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT90PWM1-16M', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_7x7mm_P0.65mm_EP4.65x4.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc4378.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller LightingAVR PWM', 'kicadSymbolki_description': '16MHz, 8kB Flash, 512B SRAM, 512B EEPROM, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_AVR : AT90PWM1-16M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

