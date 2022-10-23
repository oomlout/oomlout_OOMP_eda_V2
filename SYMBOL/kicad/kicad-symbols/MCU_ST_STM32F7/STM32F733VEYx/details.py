
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F733VEYx"
    hexID = "SZKMCUSTSTM32F7STM32F733VEYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F733VEYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-100_Die452', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00330507.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x3', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 512KB flash, 192KB RAM, 216MHz, 1.7-3.6V, 79 GPIO, WLCSP-100', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die452*'}])
    newPart['name'].append('STM32F733VEYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

