
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F429IEHx"
    hexID = "SZKMCUSTSTM32F4STM32F429IEHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F429IEHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-201_10x10mm_Layout15x15_P0.65mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00071990.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F429/439', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 192KB RAM, 180MHz, 1.8-3.6V, 140 GPIO, UFBGA-176', 'kicadSymbolki_fp_filters': 'UFBGA*10x10mm*Layout15x15*P0.65mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F429IEHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

