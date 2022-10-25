
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F401CDYx"
    hexID = "SZKMCUSTSTM32F4STM32F41CDYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F401CDYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die433', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00102166.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F401', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 384KB flash, 96KB RAM, 84MHz, 1.7-3.6V, 36 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die433*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F401CDYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

