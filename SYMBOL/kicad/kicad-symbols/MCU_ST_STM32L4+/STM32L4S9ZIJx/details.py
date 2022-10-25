
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4+"
    oIndex = "STM32L4S9ZIJx"
    hexID = "SZKMCUSTSTM32L4+STM32L4S9ZIJX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L4S9ZIJx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-144_10x10mm_Layout12x12_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00366449.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4+ STM32L4R9/S9', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 640KB RAM, 120MHz, 1.71-3.6V, 112 GPIO, UFBGA-144', 'kicadSymbolki_fp_filters': 'UFBGA*10x10mm*Layout12x12*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32L4+ : STM32L4S9ZIJx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

