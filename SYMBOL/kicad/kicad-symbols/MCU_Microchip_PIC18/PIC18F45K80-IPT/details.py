
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F45K80-IPT"
    hexID = "SZKMCUMCHIPPIC18PIC18F45K8IPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F45K80-IPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39977f.pdf', 'kicadSymbolki_keywords': 'microcontroller Flash EEPROM SPI I2C CAN UART USART ADC TQFP', 'kicadSymbolki_description': '32K Flash, 3.5K RAM, 1K EEPROM, Microchip PIC18F series enhanced flash microcontroller with ECAN and nanoWatt XLP Technology in TQFP-44 package', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F45K80-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

