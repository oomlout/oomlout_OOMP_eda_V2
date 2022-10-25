
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F45K80-IML"
    hexID = "SZKMCUMCHIPPIC18PIC18F45K8IML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F45K80-IML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PIC18F66K80%20FAMILY%20Enhanced%20Flash%20MCU%20with%20ECAN%20XLP%20Technology%2030009977G.pdf', 'kicadSymbolki_keywords': 'microcontroller Flash EEPROM SPI I2C CAN UART USART ADC', 'kicadSymbolki_description': '32K Flash, 3.5K RAM, 1K EEPROM, Microchip PIC18F series enhanced flash microcontroller with ECAN and nanoWatt XLP Technology in QFN-44 package', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F45K80-IML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

