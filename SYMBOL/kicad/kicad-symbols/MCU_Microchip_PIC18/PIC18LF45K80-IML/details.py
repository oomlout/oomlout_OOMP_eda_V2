
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF45K80-IML"
    hexID = "SZKMCUMCHIPPIC18PIC18LF45K8IML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F45K80-IML', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF45K80-IML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39977f.pdf', 'kicadSymbolki_keywords': 'microchip microcontroller PIC18 flash ECAN XLP nanoWatt', 'kicadSymbolki_description': '32K Flash, 3.5K RAM, 1K EEPROM PIC18 Microcontroller ADC PWM CAN SPI I2C USART in QFN44 package', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.65mm*'}])
    newPart['name'].append('PIC18LF45K80-IML')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

