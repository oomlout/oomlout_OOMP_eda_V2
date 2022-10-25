
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F0"
    oIndex = "STM32F072VBHx"
    hexID = "SZKMCUSTSTM32FSTM32F72VBHX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F072V8Hx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F072VBHx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-100_7x7mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00090510.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M0 STM32F0 STM32F0x2', 'kicadSymbolki_description': 'ARM Cortex-M0 MCU, 128KB flash, 16KB RAM, 48MHz, 2-3.6V, 87 GPIO, UFBGA-100', 'kicadSymbolki_fp_filters': 'UFBGA*7x7mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM32F0 : STM32F072VBHx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

