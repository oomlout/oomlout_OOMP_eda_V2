
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F765BITx"
    hexID = "SZKMCUSTSTM32F7STM32F765BITX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F765BGTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F765BITx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-208_28x28mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00273119.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x5', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 2048KB flash, 384KB RAM, 216MHz, 1.7-3.6V, 168 GPIO, LQFP-208', 'kicadSymbolki_fp_filters': 'LQFP*28x28mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F765BITx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

