
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F765VIHx"
    hexID = "SZKMCUSTSTM32F7STM32F765VIHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F765VGHx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F765VIHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-100_8x8mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00273119.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x5', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 2048KB flash, 384KB RAM, 82 GPIO, TFBGA-100', 'kicadSymbolki_fp_filters': 'TFBGA*8x8mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('STM32F765VIHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

