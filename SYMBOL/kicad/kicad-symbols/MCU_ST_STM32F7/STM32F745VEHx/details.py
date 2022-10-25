
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F745VEHx"
    hexID = "SZKMCUSTSTM32F7STM32F745VEHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F745VEHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-100_8x8mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00166116.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x5', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 512KB flash, 320KB RAM, 216MHz, 1.7-3.6V, 82 GPIO, TFBGA-100', 'kicadSymbolki_fp_filters': 'TFBGA*8x8mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F745VEHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

