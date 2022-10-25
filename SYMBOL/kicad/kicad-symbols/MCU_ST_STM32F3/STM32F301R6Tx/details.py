
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F301R6Tx"
    hexID = "SZKMCUSTSTM32F3STM32F31R6TX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F301R6Tx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00093332.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F301', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 32KB flash, 16KB RAM, 72MHz, 2-3.6V, 51 GPIO, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F301R6Tx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

