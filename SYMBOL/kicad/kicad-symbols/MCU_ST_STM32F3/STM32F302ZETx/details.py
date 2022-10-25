
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F302ZETx"
    hexID = "SZKMCUSTSTM32F3STM32F32ZETX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F302ZDTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F302ZETx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00133117.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F302', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 64KB RAM, 72MHz, 2-3.6V, 115 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F302ZETx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

