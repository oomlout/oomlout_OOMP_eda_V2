
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F303VCYx"
    hexID = "SZKMCUSTSTM32F3STM32F33VCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F303VCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-100_Die422', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00058181.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F303', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 40KB RAM, 72MHz, 2-3.6V, 78 GPIO, WLCSP-100', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die422*'}])
    newPart['name'].append('STM32F303VCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

