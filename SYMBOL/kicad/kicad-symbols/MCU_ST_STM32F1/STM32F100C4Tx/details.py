
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F100C4Tx"
    hexID = "SZKMCUSTSTM32F1STM32F1C4TX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F100C4Tx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00251732.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F100 Value Line', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 16KB flash, 4KB RAM, 24MHz, 2-3.6V, 37 GPIO, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F100C4Tx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

