
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F303C8Yx"
    hexID = "SZKMCUSTSTM32F3STM32F33C8YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F303C8Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die438', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00092070.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F303', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 64KB flash, 12KB RAM, 72MHz, 2-3.6V, 38 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die438*'}])
    newPart['name'].append('STM32F303C8Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

