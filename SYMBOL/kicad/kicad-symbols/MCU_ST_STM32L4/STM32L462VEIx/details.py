
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L462VEIx"
    hexID = "SZKMCUSTSTM32L4STM32L462VEIX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L462VEIx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-100_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00340637.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x2', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 160KB RAM, 80MHz, 1.71-3.6V, 83 GPIO, UFBGA-100', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32L4 : STM32L462VEIx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

