
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM8"
    oIndex = "STM8AL318AT"
    hexID = "SZKMCUSTSTM8STM8AL318AT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM8AL318AT', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_14x14mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm8al3188.pdf', 'kicadSymbolki_keywords': 'STM8 automotive ultra-low-power', 'kicadSymbolki_description': 'Automotive 8-bit ultra-low-power MCU, 64-Kbyte Flash, LQFP-80', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.65mm*'}])
    newPart['name'].append('STM8AL318AT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

