
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L476MGYx"
    hexID = "SZKMCUSTSTM32L4STM32L476MGYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L476MEYx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L476MGYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-81_Die415', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00108832.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x6', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 128KB RAM, 80MHz, 1.71-3.6V, 65 GPIO, WLCSP-81', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die415*'}])
    newPart['name'].append('MCU_ST_STM32L4 : STM32L476MGYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

