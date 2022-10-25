
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L041F6Px"
    hexID = "SZKMCUSTSTM32LSTM32L41F6PX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L041F6Px', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00152023.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x1', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 32KB flash, 8KB RAM, 32MHz, 1.65-3.6V, 15 GPIO, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('MCU_ST_STM32L0 : STM32L041F6Px')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

