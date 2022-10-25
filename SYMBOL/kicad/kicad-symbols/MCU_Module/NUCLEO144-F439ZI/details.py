
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "NUCLEO144-F439ZI"
    hexID = "SZKMCUMONUCLEO144F439ZI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NUCLEO144-F429ZI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUCLEO144-F439ZI', 'kicadSymbolFootprint': 'Module:ST_Morpho_Connector_144_STLink', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/user_manual/dm00244518-stm32-nucleo144-boards-stmicroelectronics.pdf', 'kicadSymbolki_keywords': 'STM32 Nucleo ST', 'kicadSymbolki_description': 'Nucleo 144 Development Board with STM32F439ZIT6 MCU, 256kB RAM, 2Mb FLASH', 'kicadSymbolki_fp_filters': 'ST*Morpho*Connector*144*STLink*'}])
    newPart['name'].append('MCU_Module : NUCLEO144-F439ZI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

