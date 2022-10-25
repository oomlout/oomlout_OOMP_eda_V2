
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F411CEYx"
    hexID = "SZKMCUSTSTM32F4STM32F411CEYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F411CCYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F411CEYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die431', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00115249.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F411', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 128KB RAM, 100MHz, 1.7-3.6V, 36 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die431*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F411CEYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

