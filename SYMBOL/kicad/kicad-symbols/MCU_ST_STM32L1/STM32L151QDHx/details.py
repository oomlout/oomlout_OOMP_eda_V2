
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L1"
    oIndex = "STM32L151QDHx"
    hexID = "SZKMCUSTSTM32L1STM32L151QDHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L151QDHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-132_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00034689.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32L1 STM32L151/152', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 384KB flash, 48KB RAM, 32MHz, 1.65-3.6V, 112 GPIO, UFBGA-132', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32L1 : STM32L151QDHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

