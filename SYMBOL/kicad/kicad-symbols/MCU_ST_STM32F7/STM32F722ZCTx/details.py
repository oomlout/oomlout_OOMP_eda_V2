
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F722ZCTx"
    hexID = "SZKMCUSTSTM32F7STM32F722ZCTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F722ZCTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00330506.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x2', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 256KB flash, 192KB RAM, 216MHz, 1.7-3.6V, 114 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F722ZCTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

