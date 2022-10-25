
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L1"
    oIndex = "STM32L151RCYx"
    hexID = "SZKMCUSTSTM32L1STM32L151RCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L151RCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-64_Die427', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00048356.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32L1 STM32L151/152', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 256KB flash, 32KB RAM, 32MHz, 1.65-3.6V, 51 GPIO, WLCSP-64', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die427*'}])
    newPart['name'].append('MCU_ST_STM32L1 : STM32L151RCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

