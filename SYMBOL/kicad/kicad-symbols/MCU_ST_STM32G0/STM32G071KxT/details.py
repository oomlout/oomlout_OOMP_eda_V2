
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32G0"
    oIndex = "STM32G071KxT"
    hexID = "SZKMCUSTSTM32GSTM32G71KXT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32G071KxT', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm32g071kb.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32G0 STM32G071', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 64/128 kB flash, 36 kB SRAM, 64 MHz, 1.7-3.6 V, 30 GPIO, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32G0 : STM32G071KxT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

