
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF26K83-xSP"
    hexID = "SZKMCUMCHIPPIC18PIC18LF26K83XSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F25K83-xSP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF26K83-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf', 'kicadSymbolki_keywords': 'microcontroller Microchip DMA WWDT DIA DCI XLP CLC CWG CCP NCO DSM CRC UART LIN DMX DALI SPI CAN I2C PPS SMT ADC2 CVD DAC', 'kicadSymbolki_description': '64K Flash, 4K RAM, 1K EEPROM, 1.8-3.6V, PIC18, low-power microcontroller with CAN, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF26K83-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

