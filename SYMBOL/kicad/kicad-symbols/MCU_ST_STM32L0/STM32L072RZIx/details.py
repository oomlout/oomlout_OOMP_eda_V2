
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L0"
    oIndex = "STM32L072RZIx"
    hexID = "SZKMCUSTSTM32LSTM32L72RZIX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L072RBIx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L072RZIx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00141133.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0+ STM32L0 STM32L0x2', 'kicadSymbolki_description': 'ARM Cortex-M0+ MCU, 192KB flash, 20KB RAM, 32MHz, 1.65-3.6V, 50 GPIO, UFBGA-64', 'kicadSymbolki_fp_filters': 'UFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('STM32L072RZIx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

