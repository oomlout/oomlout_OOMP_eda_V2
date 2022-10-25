
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F103ZGHx"
    hexID = "SZKMCUSTSTM32F1STM32F13ZGHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F103ZFHx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F103ZGHx', 'kicadSymbolFootprint': 'Package_BGA:LFBGA-144_10x10mm_Layout12x12_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00253742.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F103', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 1024KB flash, 96KB RAM, 72MHz, 2-3.6V, 114 GPIO, LFBGA-144', 'kicadSymbolki_fp_filters': 'LFBGA*10x10mm*Layout12x12*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F103ZGHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

