
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L431CCYx"
    hexID = "SZKMCUSTSTM32L4STM32L431CCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L431CBYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L431CCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die435', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00257211.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x1', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 64KB RAM, 80MHz, 1.71-3.6V, 39 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die435*'}])
    newPart['name'].append('STM32L431CCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

