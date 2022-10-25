
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AP62250Z6"
    hexID = "SZKREGULATORSWITCHINGAP6225Z6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP62150Z6', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP62250Z6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-563', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP62250.pdf', 'kicadSymbolki_keywords': '2.5A 1.3MHz PWM Buck DC/DC', 'kicadSymbolki_description': '2.5A, 1.3MHz Buck DC/DC Converter, adjustable output voltage, SOT-563', 'kicadSymbolki_fp_filters': 'SOT?563*'}])
    newPart['name'].append('Regulator_Switching : AP62250Z6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

