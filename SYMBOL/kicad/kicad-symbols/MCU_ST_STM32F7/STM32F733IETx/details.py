
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F733IETx"
    hexID = "SZKMCUSTSTM32F7STM32F733IETX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F733IETx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-176_24x24mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00330507.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x3', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 512KB flash, 192KB RAM, 216MHz, 1.7-3.6V, 138 GPIO, LQFP-176', 'kicadSymbolki_fp_filters': 'LQFP*24x24mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F733IETx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

