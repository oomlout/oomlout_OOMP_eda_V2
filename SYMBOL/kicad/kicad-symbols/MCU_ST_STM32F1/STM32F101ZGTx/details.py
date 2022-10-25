
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F101ZGTx"
    hexID = "SZKMCUSTSTM32F1STM32F11ZGTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F101ZFTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F101ZGTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00253739.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F101', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 1024KB flash, 80KB RAM, 36MHz, 2-3.6V, 114 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F101ZGTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

