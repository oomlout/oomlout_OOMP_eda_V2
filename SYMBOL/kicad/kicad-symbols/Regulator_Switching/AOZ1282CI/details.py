
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AOZ1282CI"
    hexID = "SZKREGULATORSWITCHINGAOZ1282CI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AOZ1280CI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AOZ1282CI', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://aosmd.com/res/data_sheets/AOZ1282CI.pdf', 'kicadSymbolki_keywords': 'switching buck converter', 'kicadSymbolki_description': '1.2 A Simple Buck Regulator, 4.5-36V input, 450kHz', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : AOZ1282CI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

