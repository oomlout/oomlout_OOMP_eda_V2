
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F071C8Ux"
    hexID = "SZKMCUSTSTM32FSTM32F71C8UX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F071C8Ux', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00098745.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x1', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 64KB flash, 16KB RAM, 48MHz, 2-3.6V, 37 GPIO, UFQFPN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F071C8Ux')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

