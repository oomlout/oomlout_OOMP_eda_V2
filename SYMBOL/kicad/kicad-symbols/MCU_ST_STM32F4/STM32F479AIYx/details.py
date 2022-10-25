
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F479AIYx"
    hexID = "SZKMCUSTSTM32F4STM32F479AIYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F479AGYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F479AIYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-168_Die434', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00208574.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F469/479', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 320KB RAM, 180MHz, 1.7-3.6V, 128 GPIO, WLCSP-168', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die434*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F479AIYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

