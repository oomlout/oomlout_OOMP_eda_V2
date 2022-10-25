
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F25K20_ISS"
    hexID = "SZKMCUMCHIPPIC18PIC18F25K2ISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F23K20_ISS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F25K20_ISS', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001303H.pdf', 'kicadSymbolki_keywords': 'microcontroller PIC18F flash XLP', 'kicadSymbolki_description': '32K Flash, 1536Byte RAM, 256Byte EEPROM, PIC18 Microcontroller ADC PWM SPI I2C USART in SSOP28 package', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F25K20_ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

