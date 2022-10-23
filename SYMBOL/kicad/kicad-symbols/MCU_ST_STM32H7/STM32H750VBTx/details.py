
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32H7"
    oIndex = "STM32H750VBTx"
    hexID = "SZKMCUSTSTM32H7STM32H75VBTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32H753VITx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32H750VBTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm32h750ib.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M7 STM32H7', 'kicadSymbolki_description': 'ARM Cortex-M7 MCU, 128KB flash, 864KB RAM, 480MHz, 1.7-3.6V, 82 GPIO, LQFP-100', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('STM32H750VBTx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

