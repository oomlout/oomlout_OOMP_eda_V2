
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F030C6Tx"
    hexID = "SZKMCUSTSTM32FSTM32F3C6TX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F030C6Tx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00088500.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x0 Value Line', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 32KB flash, 4KB RAM, 48MHz, 2.4-3.6V, 39 GPIO, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F030C6Tx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

