
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "NUCLEO144-F207ZG"
    hexID = "SZKMCUMONUCLEO144F27ZG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NUCLEO144-F429ZI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUCLEO144-F207ZG', 'kicadSymbolFootprint': 'Module:ST_Morpho_Connector_144_STLink', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/user_manual/dm00244518-stm32-nucleo144-boards-stmicroelectronics.pdf', 'kicadSymbolki_keywords': 'STM32 Nucleo ST', 'kicadSymbolki_description': 'Nucleo 144 Development Board with STM32F207ZGT6 MCU, 128+4Kb RAM, 1Mb FLASH', 'kicadSymbolki_fp_filters': 'ST*Morpho*Connector*144*STLink*'}])
    newPart['name'].append('NUCLEO144-F207ZG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

