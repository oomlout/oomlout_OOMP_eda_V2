
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F469BETx"
    hexID = "SZKMCUSTSTM32F4STM32F469BETX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F469BETx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-208_28x28mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00219980.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F469/479', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 320KB RAM, 180MHz, 1.7-3.6V, 159 GPIO, LQFP-208', 'kicadSymbolki_fp_filters': 'LQFP*28x28mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F469BETx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

