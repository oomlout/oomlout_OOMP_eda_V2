
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F303VEHx"
    hexID = "SZKMCUSTSTM32F3STM32F33VEHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F303VDHx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F303VEHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-100_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00118585.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F303', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 64KB RAM, 72MHz, 2-3.6V, 86 GPIO, UFBGA-100', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('STM32F303VEHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

