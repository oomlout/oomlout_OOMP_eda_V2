
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F051K8Ux"
    hexID = "SZKMCUSTSTM32FSTM32F51K8UX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F051K8Ux', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00039193.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x1', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 64KB flash, 8KB RAM, 48MHz, 2-3.6V, 27 GPIO, UFQFPN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F051K8Ux')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

