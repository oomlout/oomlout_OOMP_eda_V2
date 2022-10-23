
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F373VBHx"
    hexID = "SZKMCUSTSTM32F3STM32F373VBHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F373V8Hx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F373VBHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-100_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00046749.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F373', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 128KB flash, 24KB RAM, 72MHz, 2-3.6V, 84 GPIO, UFBGA-100', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('STM32F373VBHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

