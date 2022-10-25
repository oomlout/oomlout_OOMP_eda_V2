
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F103R8Hx"
    hexID = "SZKMCUSTSTM32F1STM32F13R8HX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F103R8Hx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00161566.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F103', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 64KB flash, 20KB RAM, 72MHz, 2-3.6V, 50 GPIO, TFBGA-64', 'kicadSymbolki_fp_filters': 'TFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F103R8Hx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

