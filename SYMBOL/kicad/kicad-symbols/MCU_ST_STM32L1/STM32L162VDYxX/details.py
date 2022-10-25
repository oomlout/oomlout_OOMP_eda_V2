
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L1"
    oIndex = "STM32L162VDYxX"
    hexID = "SZKMCUSTSTM32L1STM32L162VDYXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L162VDYxX', 'kicadSymbolFootprint': 'Package_CSP:ST_WLCSP-104_Die437', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00039232.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32L1 STM32L162', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 384KB flash, 80KB RAM, 32MHz, 1.65-3.6V, 83 GPIO, WLCSP-104', 'kicadSymbolki_fp_filters': 'ST_WLCSP*Die437*'}])
    newPart['name'].append('MCU_ST_STM32L1 : STM32L162VDYxX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

