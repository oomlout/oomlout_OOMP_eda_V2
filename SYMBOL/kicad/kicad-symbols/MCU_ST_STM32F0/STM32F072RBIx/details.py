
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F072RBIx"
    hexID = "SZKMCUSTSTM32FSTM32F72RBIX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F072RBIx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00090510.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x2', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 128KB flash, 16KB RAM, 48MHz, 2-3.6V, 51 GPIO, UFBGA-64', 'kicadSymbolki_fp_filters': 'UFBGA*5x5mm*Layout8x8*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F072RBIx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

