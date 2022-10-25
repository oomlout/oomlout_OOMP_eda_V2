
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F723IEKx"
    hexID = "SZKMCUSTSTM32F7STM32F723IEKX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F723ICKx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F723IEKx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-201_10x10mm_Layout15x15_P0.65mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00330506.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x3', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 512KB flash, 192KB RAM, 216MHz, 1.7-3.6V, 138 GPIO, UFBGA-176', 'kicadSymbolki_fp_filters': 'UFBGA*10x10mm*Layout15x15*P0.65mm*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F723IEKx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

