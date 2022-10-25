
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F429ZGYx"
    hexID = "SZKMCUSTSTM32F4STM32F429ZGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F429ZGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-143_Die419', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00071990.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F429/439', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 192KB RAM, 180MHz, 1.8-3.6V, 114 GPIO, WLCSP-143', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die419*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F429ZGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

