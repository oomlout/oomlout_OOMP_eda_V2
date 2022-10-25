
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F446ZCTx"
    hexID = "SZKMCUSTSTM32F4STM32F446ZCTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F446ZCTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00141306.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F446', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 128KB RAM, 180MHz, 1.8-3.6V, 114 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F446ZCTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

