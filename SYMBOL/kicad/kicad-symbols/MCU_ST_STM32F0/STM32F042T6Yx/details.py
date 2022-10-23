
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F042T6Yx"
    hexID = "SZKMCUSTSTM32FSTM32F42T6YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F042T6Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-36_Die445', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00105814.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x2', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 32KB flash, 6KB RAM, 48MHz, 2-3.6V, 30 GPIO, WLCSP-36', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die445*'}])
    newPart['name'].append('STM32F042T6Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

