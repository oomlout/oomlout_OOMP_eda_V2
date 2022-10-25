
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM8"
    oIndex = "STM8L152R6T"
    hexID = "SZKMCUSTSTM8STM8L152R6T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM8L152R8T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM8L152R6T', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm8l152r6.pdf', 'kicadSymbolki_keywords': 'STM8L Microcontroller Low Power LCD', 'kicadSymbolki_description': '16MHz, 32K Flash, 2K EEPROM, LCD, USART, I²C, SPI, ADC, DAC, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM8 : STM8L152R6T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

