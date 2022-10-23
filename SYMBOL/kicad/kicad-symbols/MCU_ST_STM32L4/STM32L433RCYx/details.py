
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L433RCYx"
    hexID = "SZKMCUSTSTM32L4STM32L433RCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L433RBYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L433RCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-64_Die435', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00257192.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x3', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 64KB RAM, 80MHz, 1.71-3.6V, 52 GPIO, WLCSP-64', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die435*'}])
    newPart['name'].append('STM32L433RCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

