
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F437AIHx"
    hexID = "SZKMCUSTSTM32F4STM32F437AIHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F437AIHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-169_7x7mm_Layout13x13_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00077036.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F427/437', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 192KB RAM, 180MHz, 1.7-3.6V, 130 GPIO, UFBGA-169', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout13x13*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F437AIHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

