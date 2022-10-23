
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32H7"
    oIndex = "STM32H750IBKx"
    hexID = "SZKMCUSTSTM32H7STM32H75IBKX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32H753IIKx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32H750IBKx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-201_10x10mm_Layout15x15_P0.65mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm32h750ib.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32H7', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 128KB flash, 864KB RAM, 480MHz, 1.7-3.6V, 140 GPIO, UFBGA-176', 'kicadSymbolki_fp_filters': 'UFBGA*10x10mm*Layout15x15*P0.65mm*'}])
    newPart['name'].append('STM32H750IBKx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

