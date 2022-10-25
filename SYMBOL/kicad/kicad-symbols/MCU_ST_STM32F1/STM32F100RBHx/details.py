
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F100RBHx"
    hexID = "SZKMCUSTSTM32F1STM32F1RBHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F100R8Hx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F100RBHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00251732.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F100 Value Line', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 128KB flash, 8KB RAM, 24MHz, 2-3.6V, 50 GPIO, TFBGA-64', 'kicadSymbolki_fp_filters': 'TFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F100RBHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

