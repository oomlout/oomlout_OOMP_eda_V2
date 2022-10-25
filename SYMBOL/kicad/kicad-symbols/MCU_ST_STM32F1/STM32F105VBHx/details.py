
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F105VBHx"
    hexID = "SZKMCUSTSTM32F1STM32F15VBHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F105V8Hx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F105VBHx', 'kicadSymbolFootprint': 'Package_BGA:LFBGA-100_10x10mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00220364.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F105/107', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 128KB flash, 64KB RAM, 72MHz, 2-3.6V, 82 GPIO, LFBGA-100', 'kicadSymbolki_fp_filters': 'LFBGA*10x10mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F105VBHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

