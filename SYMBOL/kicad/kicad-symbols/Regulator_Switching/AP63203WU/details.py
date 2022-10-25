
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AP63203WU"
    hexID = "SZKREGULATORSWITCHINGAP6323WU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP63200WU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP63203WU', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf', 'kicadSymbolki_keywords': '2A Buck DC/DC', 'kicadSymbolki_description': '2A, 1.1MHz Buck DC/DC Converter, fixed 3.3V output voltage, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : AP63203WU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

