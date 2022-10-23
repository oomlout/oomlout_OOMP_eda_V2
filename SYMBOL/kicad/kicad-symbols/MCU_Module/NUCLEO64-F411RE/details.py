
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "NUCLEO64-F411RE"
    hexID = "SZKMCUMONUCLEO64F411RE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUCLEO64-F411RE', 'kicadSymbolFootprint': 'Module:ST_Morpho_Connector_144_STLink', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/data_brief/DM00105918.pdf', 'kicadSymbolki_keywords': 'STM32 Nucleo ST', 'kicadSymbolki_description': 'Nucleo 64 Development Board with STM32F411RET6 MCU, 128kB RAM, 512KB FLASH', 'kicadSymbolki_fp_filters': 'ST*Morpho*Connector*144*STLink*'}])
    newPart['name'].append('NUCLEO64-F411RE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

