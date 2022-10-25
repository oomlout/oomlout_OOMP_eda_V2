
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32H7"
    oIndex = "STM32H753XIHx"
    hexID = "SZKMCUSTSTM32H7STM32H753XIHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32H753XIHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-265_14x14mm_Layout17x17_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00388325.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32H7 STM32H7x3', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 2048KB flash, 864KB RAM, 400MHz, 1.7-3.6V, 168 GPIO, TFBGA-240', 'kicadSymbolki_fp_filters': 'TFBGA*14x14mm*Layout17x17*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32H7 : STM32H753XIHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

