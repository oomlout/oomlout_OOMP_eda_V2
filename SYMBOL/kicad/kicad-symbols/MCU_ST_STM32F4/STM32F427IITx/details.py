
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F427IITx"
    hexID = "SZKMCUSTSTM32F4STM32F427IITX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F427IGTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F427IITx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-176_24x24mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00071990.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F427/437', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 192KB RAM, 180MHz, 1.7-3.6V, 140 GPIO, LQFP-176', 'kicadSymbolki_fp_filters': 'LQFP*24x24mm*P0.5mm*'}])
    newPart['name'].append('STM32F427IITx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

