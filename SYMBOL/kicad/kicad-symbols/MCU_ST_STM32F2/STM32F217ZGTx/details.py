
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F2"
    oIndex = "STM32F217ZGTx"
    hexID = "SZKMCUSTSTM32F2STM32F217ZGTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F217ZETx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F217ZGTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00263874.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F2 STM32F2x7', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 1024KB flash, 128KB RAM, 120MHz, 1.8-3.6V, 114 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F2 : STM32F217ZGTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

