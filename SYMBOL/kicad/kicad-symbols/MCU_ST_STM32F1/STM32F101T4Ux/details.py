
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F1"
    oIndex = "STM32F101T4Ux"
    hexID = "SZKMCUSTSTM32F1STM32F11T4UX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F101T4Ux', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-36-1EP_6x6mm_P0.5mm_EP4.1x4.1mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00210837.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F1 STM32F101', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 16KB flash, 4KB RAM, 36MHz, 2-3.6V, 26 GPIO, VFQFPN-36', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.5mm*'}])
    newPart['name'].append('STM32F101T4Ux')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

