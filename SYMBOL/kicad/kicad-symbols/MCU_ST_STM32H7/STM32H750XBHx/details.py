
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32H7"
    oIndex = "STM32H750XBHx"
    hexID = "SZKMCUSTSTM32H7STM32H75XBHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32H753XIHx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32H750XBHx', 'kicadSymbolFootprint': 'Package_BGA:TFBGA-265_14x14mm_Layout17x17_P0.8mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm32h750ib.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32H7', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 128KB flash, 864KB RAM, 480MHz, 1.7-3.6V, 168 GPIO, TFBGA-240', 'kicadSymbolki_fp_filters': 'TFBGA*14x14mm*Layout17x17*P0.8mm*'}])
    newPart['name'].append('STM32H750XBHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

