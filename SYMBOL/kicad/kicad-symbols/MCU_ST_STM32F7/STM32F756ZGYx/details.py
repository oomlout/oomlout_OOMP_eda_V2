
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F756ZGYx"
    hexID = "SZKMCUSTSTM32F7STM32F756ZGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F756ZGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-143_Die449', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00166114.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x6', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 1024KB flash, 320KB RAM, 216MHz, 1.7-3.6V, 114 GPIO, WLCSP-143', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die449*'}])
    newPart['name'].append('STM32F756ZGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

