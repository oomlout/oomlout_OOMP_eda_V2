
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L052T6Yx"
    hexID = "SZKMCUSTSTM32LSTM32L52T6YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L052T6Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-36_Die417', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00108217.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x2', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 32KB flash, 8KB RAM, 32MHz, 1.65-3.6V, 29 GPIO, WLCSP-36', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die417*'}])
    newPart['name'].append('STM32L052T6Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

