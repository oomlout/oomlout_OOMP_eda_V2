
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F318C8Yx"
    hexID = "SZKMCUSTSTM32F3STM32F318C8YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F318C8Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die439', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00115350.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F3x8', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 64KB flash, 16KB RAM, 72MHz, 1.65-1.95V, 36 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die439*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F318C8Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

