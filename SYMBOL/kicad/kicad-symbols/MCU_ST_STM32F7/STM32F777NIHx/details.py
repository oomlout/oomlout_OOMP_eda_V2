
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F777NIHx"
    hexID = "SZKMCUSTSTM32F7STM32F777NIHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F777NIHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-216_13x13mm_Layout15x15_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00225424.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x7', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 2048KB flash, 384KB RAM, 216MHz, 1.7-3.6V, 168 GPIO, TFBGA-216', 'kicadSymbolki_fp_filters': 'TFBGA*13x13mm*Layout15x15*P0.8mm*'}])
    newPart['name'].append('STM32F777NIHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

