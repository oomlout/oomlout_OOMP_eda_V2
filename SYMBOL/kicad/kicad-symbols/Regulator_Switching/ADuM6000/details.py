
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADuM6000"
    hexID = "SZKREGULATORSWITCHINGADUM6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM6000', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM6000.PDF', 'kicadSymbolki_keywords': 'Isolated DC-to-DC Converter 5kV', 'kicadSymbolki_description': 'Isolated 5 kV DC-to-DC Converter', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm* SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : ADuM6000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

