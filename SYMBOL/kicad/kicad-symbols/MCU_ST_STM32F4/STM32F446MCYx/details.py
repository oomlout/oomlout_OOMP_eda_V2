
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F446MCYx"
    hexID = "SZKMCUSTSTM32F4STM32F446MCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F446MCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-81_Die421', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00141306.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F446', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 128KB RAM, 180MHz, 1.8-3.6V, 63 GPIO, WLCSP-81', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die421*'}])
    newPart['name'].append('STM32F446MCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

