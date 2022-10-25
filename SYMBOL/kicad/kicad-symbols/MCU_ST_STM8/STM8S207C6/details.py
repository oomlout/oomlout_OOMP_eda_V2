
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM8"
    oIndex = "STM8S207C6"
    hexID = "SZKMCUSTSTM8STM8S27C6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM8S208CB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM8S207C6', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm8s208cb.pdf', 'kicadSymbolki_keywords': 'STM8 Microcontroller Performance Line', 'kicadSymbolki_description': '24MHz, 32K Flash, 2K EEPROM, 10-bit ADC, 2 UARTs, SPI, I²C, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM8 : STM8S207C6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

