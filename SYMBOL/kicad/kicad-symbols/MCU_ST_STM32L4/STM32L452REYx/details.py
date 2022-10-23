
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L452REYx"
    hexID = "SZKMCUSTSTM32L4STM32L452REYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L452RCYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L452REYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-64_Die462', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00340549.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x2', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 160KB RAM, 80MHz, 1.71-3.6V, 52 GPIO, WLCSP-64', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die462*'}])
    newPart['name'].append('STM32L452REYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

