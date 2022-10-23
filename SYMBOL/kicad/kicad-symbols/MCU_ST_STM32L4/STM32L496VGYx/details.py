
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L496VGYx"
    hexID = "SZKMCUSTSTM32L4STM32L496VGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L496VEYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L496VGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-100_Die461', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00284211.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x6', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 320KB RAM, 80MHz, 1.71-3.6V, 81 GPIO, WLCSP-100', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die461*'}])
    newPart['name'].append('STM32L496VGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

