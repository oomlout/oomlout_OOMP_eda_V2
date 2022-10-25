
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF25K80_ISS"
    hexID = "SZKMCUMCHIPPIC18PIC18LF25K8ISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F25K80_ISS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF25K80_ISS', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39977f.pdf', 'kicadSymbolki_keywords': 'microchip microcontroller PIC18 flash ECAN XLP nanoWatt', 'kicadSymbolki_description': '32K Flash, 3.5K RAM, 1K EEPROM PIC18 Microcontroller ADC PWM CAN SPI I2C USART in SSOP28 package', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF25K80_ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

