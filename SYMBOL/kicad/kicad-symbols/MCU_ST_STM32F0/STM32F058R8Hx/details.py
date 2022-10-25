
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F058R8Hx"
    hexID = "SZKMCUSTSTM32FSTM32F58R8HX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F058R8Hx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00059126.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x8', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 64KB flash, 8KB RAM, 48MHz, 1.65-1.95V, 54 GPIO, UFBGA-64', 'kicadSymbolki_fp_filters': 'UFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F058R8Hx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

