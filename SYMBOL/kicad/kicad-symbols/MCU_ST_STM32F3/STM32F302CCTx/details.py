
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F3"
    oIndex = "STM32F302CCTx"
    hexID = "SZKMCUSTSTM32F3STM32F32CCTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F302CBTx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F302CCTx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00094064.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F3 STM32F302', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 256KB flash, 40KB RAM, 72MHz, 2-3.6V, 37 GPIO, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F3 : STM32F302CCTx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

