
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "NUCLEO144-F429ZI"
    hexID = "SZKMCUMONUCLEO144F429ZI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUCLEO144-F429ZI', 'kicadSymbolFootprint': 'Module:ST_Morpho_Connector_144_STLink', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/data_brief/group0/7b/df/1d/e9/64/55/43/8d/DM00247910/files/DM00247910.pdf/jcr:content/translations/en.DM00247910.pdf', 'kicadSymbolki_keywords': 'STM32 Nucleo ST', 'kicadSymbolki_description': 'Nucleo 144 Development Board with STM32F429ZIT6 MCU, 256kB RAM, 1Mb FLASH', 'kicadSymbolki_fp_filters': 'ST*Morpho*Connector*144*STLink*'}])
    newPart['name'].append('MCU_Module : NUCLEO144-F429ZI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

