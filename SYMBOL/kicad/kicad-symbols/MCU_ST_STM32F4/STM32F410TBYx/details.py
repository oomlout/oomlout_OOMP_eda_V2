
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F410TBYx"
    hexID = "SZKMCUSTSTM32F4STM32F41TBYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F410T8Yx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F410TBYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-36_Die458', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00214043.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F410', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 128KB flash, 32KB RAM, 100MHz, 1.7-3.6V, 23 GPIO, WLCSP-36', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die458*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F410TBYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

