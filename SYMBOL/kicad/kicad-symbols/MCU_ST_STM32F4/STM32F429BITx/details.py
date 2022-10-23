
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F429BITx"
    hexID = "SZKMCUSTSTM32F4STM32F429BITX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F429BETx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F429BITx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-208_28x28mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00071990.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F429/439', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 2048KB flash, 192KB RAM, 180MHz, 1.8-3.6V, 168 GPIO, LQFP-208', 'kicadSymbolki_fp_filters': 'LQFP*28x28mm*P0.5mm*'}])
    newPart['name'].append('STM32F429BITx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

