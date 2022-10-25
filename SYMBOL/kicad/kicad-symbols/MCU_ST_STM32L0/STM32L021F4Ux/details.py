
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L021F4Ux"
    hexID = "SZKMCUSTSTM32LSTM32L21F4UX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L021F4Ux', 'kicadSymbolFootprint': 'Package_DFN_QFN:ST_UFQFPN-20_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00206858.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x1', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 16KB flash, 2KB RAM, 32MHz, 1.65-3.6V, 16 GPIO, UFQFPN-20', 'kicadSymbolki_fp_filters': 'ST*UFQFPN*3x3mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32L0 : STM32L021F4Ux')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

