
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F051T8Yx"
    hexID = "SZKMCUSTSTM32FSTM32F51T8YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F051T8Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-36_Die440', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00039193.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x1', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 64KB flash, 8KB RAM, 48MHz, 2-3.6V, 29 GPIO, WLCSP-36', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die440*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F051T8Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

