
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F373RCTx"
    hexID = "SZKMCUSTSTM32F3STM32F373RCTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F373R8Tx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F373RCTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00046749.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F373', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 32KB RAM, 72MHz, 2-3.6V, 52 GPIO, LQFP-64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F373RCTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

