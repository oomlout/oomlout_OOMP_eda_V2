
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32L4"
    oIndex = "STM32L452REIx"
    hexID = "SZKMCUSTSTM32L4STM32L452REIX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32L452RCIx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32L452REIx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00340549.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32L4 STM32L4x2', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 512KB flash, 160KB RAM, 80MHz, 1.71-3.6V, 52 GPIO, UFBGA-64', 'kicadSymbolki_fp_filters': 'UFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('STM32L452REIx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

