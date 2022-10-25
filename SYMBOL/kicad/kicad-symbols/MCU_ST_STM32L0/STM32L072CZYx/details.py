
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L072CZYx"
    hexID = "SZKMCUSTSTM32LSTM32L72CZYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L072CBYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L072CZYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die447', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00141133.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x2', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 192KB flash, 20KB RAM, 32MHz, 1.65-3.6V, 40 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die447*'}])
    newPart['name'].append('MCU_ST_STM32L0 : STM32L072CZYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

