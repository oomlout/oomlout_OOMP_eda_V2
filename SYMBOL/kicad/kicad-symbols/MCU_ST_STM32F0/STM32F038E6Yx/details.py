
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F038E6Yx"
    hexID = "SZKMCUSTSTM32FSTM32F38E6YX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F038E6Yx', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-25_Die444', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00110868.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x8', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 32KB flash, 4KB RAM, 48MHz, 1.65-1.95V, 20 GPIO, WLCSP-25', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die444*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F038E6Yx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

