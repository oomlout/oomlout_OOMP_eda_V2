
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4+"
    oIndex = "STM32L4R5ZITx"
    hexID = "SZKMCUSTSTM32L4+STM32L4R5ZITX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L4R5ZGTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L4R5ZITx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00366448.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4+ STM32L4R5/S5', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 640KB RAM, 120MHz, 1.71-3.6V, 115 GPIO, LQFP-144', 'kicadSymbolki_fp_filters': 'LQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('STM32L4R5ZITx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

