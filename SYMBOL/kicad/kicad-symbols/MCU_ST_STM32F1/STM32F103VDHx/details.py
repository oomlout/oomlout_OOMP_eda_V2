
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F103VDHx"
    hexID = "SZKMCUSTSTM32F1STM32F13VDHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F103VCHx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F103VDHx', 'kicadSymbolFootprint': 'Package_BGA:LFBGA-100_10x10mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00191185.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F103', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 384KB flash, 64KB RAM, 72MHz, 2-3.6V, 82 GPIO, LFBGA-100', 'kicadSymbolki_fp_filters': 'LFBGA*10x10mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('STM32F103VDHx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

