
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L433CBYx"
    hexID = "SZKMCUSTSTM32L4STM32L433CBYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L433CBYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-49_Die435', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00257192.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x3', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 128KB flash, 64KB RAM, 80MHz, 1.71-3.6V, 39 GPIO, WLCSP-49', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die435*'}])
    newPart['name'].append('MCU_ST_STM32L4 : STM32L433CBYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

