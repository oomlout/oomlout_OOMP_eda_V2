
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F7"
    oIndex = "STM32F769AGYx"
    hexID = "SZKMCUSTSTM32F7STM32F769AGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F769AGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-180_Die451', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00273119.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32F7 STM32F7x9', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 1024KB flash, 384KB RAM, 216MHz, 1.7-3.6V, 128 GPIO, WLCSP-180', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die451*'}])
    newPart['name'].append('MCU_ST_STM32F7 : STM32F769AGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

