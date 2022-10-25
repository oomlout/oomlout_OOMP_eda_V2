
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F048G6Ux"
    hexID = "SZKMCUSTSTM32FSTM32F48G6UX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F048G6Ux', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28_4x4mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00109264.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x8', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 32KB flash, 6KB RAM, 48MHz, 1.65-1.95V, 22 GPIO, UFQFPN-28', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F048G6Ux')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

