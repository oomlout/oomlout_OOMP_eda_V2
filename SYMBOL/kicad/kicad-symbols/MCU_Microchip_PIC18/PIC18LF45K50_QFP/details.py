
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF45K50_QFP"
    hexID = "SZKMCUMCHIPPIC18PIC18LF45K5QFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F45K50_QFP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF45K50_QFP', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30000684B.pdf', 'kicadSymbolki_keywords': 'microcontroller Flash EEPROM SPI I2C USB UART USART ADC TQFP', 'kicadSymbolki_description': '32K Flash, 2K RAM, 256B EEPROM, Microchip PIC18F series enhanced flash microcontroller with USB and nanoWatt XLP Technology in TQFP-44 package', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('PIC18LF45K50_QFP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

