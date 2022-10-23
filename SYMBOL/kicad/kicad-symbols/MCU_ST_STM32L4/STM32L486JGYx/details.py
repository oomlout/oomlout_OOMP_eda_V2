
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L486JGYx"
    hexID = "SZKMCUSTSTM32L4STM32L486JGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L486JGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-72_Die415', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00108833.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x6', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 128KB RAM, 80MHz, 1.71-3.6V, 57 GPIO, WLCSP-72', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die415*'}])
    newPart['name'].append('STM32L486JGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

