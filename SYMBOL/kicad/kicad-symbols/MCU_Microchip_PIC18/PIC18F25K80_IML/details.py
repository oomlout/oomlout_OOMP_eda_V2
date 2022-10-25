
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F25K80_IML"
    hexID = "SZKMCUMCHIPPIC18PIC18F25K8IML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F25K80_IML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_6x6mm_P0.65mm_EP4.25x4.25mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39977f.pdf', 'kicadSymbolki_keywords': 'microcontroller PIC18 flash ECAN XLP nanoWatt', 'kicadSymbolki_description': '32K Flash, 3.5K RAM, 1K EEPROM PIC18 Microcontroller ADC PWM CAN SPI I2C USART in QFN28 package', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F25K80_IML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

