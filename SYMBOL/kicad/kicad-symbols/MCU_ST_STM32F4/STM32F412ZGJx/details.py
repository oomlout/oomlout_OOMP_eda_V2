
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM32F4"
    oIndex = "STM32F412ZGJx"
    hexID = "SZKMCUSTSTM32F4STM32F412ZGJX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STM32F412ZEJx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM32F412ZGJx', 'kicadSymbolFootprint': 'Package_BGA:UFBGA-144_10x10mm_Layout12x12_P0.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00213872.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4 STM32F4 STM32F412', 'kicadSymbolki_description': 'ARM Cortex-M4 MCU, 1024KB flash, 256KB RAM, 100MHz, 1.7-3.6V, 114 GPIO, UFBGA-144', 'kicadSymbolki_fp_filters': 'UFBGA*10x10mm*Layout12x12*P0.8mm*'}])
    newPart['name'].append('MCU_ST_STM32F4 : STM32F412ZGJx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

