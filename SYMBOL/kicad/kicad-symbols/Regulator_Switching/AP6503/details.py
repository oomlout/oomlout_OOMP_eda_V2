
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AP6503"
    hexID = "SZKREGULATORSWITCHINGAP653"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP6502', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP6503', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP6503.pdf', 'kicadSymbolki_keywords': 'buck switching converter', 'kicadSymbolki_description': '340kHz 23V 3A Synchonous DC/DC Buck Converter', 'kicadSymbolki_fp_filters': 'Diodes_SO-8EP*'}])
    newPart['name'].append('Regulator_Switching : AP6503')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

