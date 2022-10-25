
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F2"
    oIndex = "STM32F217IETx"
    hexID = "SZKMCUSTSTM32F2STM32F217IETX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F217IETx', 'kicadSymbolFootprint': 'Package_QFP:LQFP-176_24x24mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00263874.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M3 STM32F2 STM32F2x7', 'kicadSymbolki_description': 'ARM Cortex-M3 MCU, 512KB flash, 128KB RAM, 120MHz, 1.8-3.6V, 140 GPIO, LQFP-176', 'kicadSymbolki_fp_filters': 'LQFP*24x24mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F2 : STM32F217IETx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

