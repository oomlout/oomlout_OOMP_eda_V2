
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32G0"
    oIndex = "STM32G071KxU"
    hexID = "SZKMCUSTSTM32GSTM32G71KXU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32G071KxU', 'kicadSymbolFootprint': 'Package_DFN_QFN:UFQFPN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm32g071kb.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32G0 STM32G071', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 64/128 kB flash, 36 kB SRAM, 64 MHz, 1.7-3.6 V, 30 GPIO, UFQFPN-32', 'kicadSymbolki_fp_filters': 'UFQFPN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32G0 : STM32G071KxU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

