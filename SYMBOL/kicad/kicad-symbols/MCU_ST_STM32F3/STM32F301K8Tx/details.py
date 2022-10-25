
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F301K8Tx"
    hexID = "SZKMCUSTSTM32F3STM32F31K8TX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F301K6Tx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F301K8Tx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00093332.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F301', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 64KB flash, 16KB RAM, 72MHz, 2-3.6V, 25 GPIO, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F301K8Tx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

