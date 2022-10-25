
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4+"
    oIndex = "STM32L4R9VGTx"
    hexID = "SZKMCUSTSTM32L4+STM32L4R9VGTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L4R9VGTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00366448.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4+ STM32L4R9/S9', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 640KB RAM, 120MHz, 1.71-3.6V, 77 GPIO, LQFP-100', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32L4+ : STM32L4R9VGTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

