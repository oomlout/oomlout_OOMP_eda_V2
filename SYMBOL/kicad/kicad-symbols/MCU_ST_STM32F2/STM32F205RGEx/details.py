
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F2"
    oIndex = "STM32F205RGEx"
    hexID = "SZKMCUSTSTM32F2STM32F25RGEX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F205RGEx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-66_Die411', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00237391.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F2 STM32F2x5', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 1024KB flash, 128KB RAM, 120MHz, 1.8-3.6V, 51 GPIO, EWLCSP-66', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die411*'}])
    newPart['name'].append('MCU_ST_STM32F2 : STM32F205RGEx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

