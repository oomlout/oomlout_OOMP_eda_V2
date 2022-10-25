
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F401CEUx"
    hexID = "SZKMCUSTSTM32F4STM32F41CEUX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F401CDUx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F401CEUx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00102166.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F401', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 96KB RAM, 84MHz, 1.7-3.6V, 36 GPIO, UFQFPN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F401CEUx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

