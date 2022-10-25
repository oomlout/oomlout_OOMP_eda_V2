
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F091VCHx"
    hexID = "SZKMCUSTSTM32FSTM32F91VCHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F091VCHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-100_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00115237.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x1', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 256KB flash, 32KB RAM, 48MHz, 2-3.6V, 88 GPIO, UFBGA-100', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F091VCHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

