
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L011E4Yx"
    hexID = "SZKMCUSTSTM32LSTM32L11E4YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L011E3Yx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L011E4Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-25_Die457', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00206508.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x1', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 16KB flash, 2KB RAM, 32MHz, 1.65-3.6V, 21 GPIO, WLCSP-25', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die457*'}])
    newPart['name'].append('MCU_ST_STM32L0 : STM32L011E4Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

