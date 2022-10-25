
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F091RCYx"
    hexID = "SZKMCUSTSTM32FSTM32F91RCYX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F091RCYx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-64_Die442', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00115237.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x1', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 256KB flash, 32KB RAM, 48MHz, 2-3.6V, 52 GPIO, WLCSP-64', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die442*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F091RCYx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

