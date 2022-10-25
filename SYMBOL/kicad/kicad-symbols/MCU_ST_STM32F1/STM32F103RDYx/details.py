
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F103RDYx"
    hexID = "SZKMCUSTSTM32F1STM32F13RDYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F103RCYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F103RDYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-64_Die414', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00191185.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F103', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 384KB flash, 64KB RAM, 72MHz, 2-3.6V, 50 GPIO, WLCSP-64', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die414*'}])
    newPart['name'].append('MCU_ST_STM32F1 : STM32F103RDYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

