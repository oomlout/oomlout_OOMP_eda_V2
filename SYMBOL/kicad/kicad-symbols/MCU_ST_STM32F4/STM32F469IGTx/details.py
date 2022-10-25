
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F469IGTx"
    hexID = "SZKMCUSTSTM32F4STM32F469IGTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F469IETx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F469IGTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-176_24x24mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00219980.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F469/479', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 320KB RAM, 180MHz, 1.7-3.6V, 131 GPIO, LQFP-176', 'kicadSymbolki_fp_filters': 'LQFP*24x24mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F469IGTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

