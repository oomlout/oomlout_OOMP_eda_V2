
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "ISL21070DIH306Z-TK"
    hexID = "SZKREFERENCEVOLTAGEISL217DIH36ZTK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL21070DIH306Z-TK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/fn75/fn7599.pdf', 'kicadSymbolki_keywords': 'Micropower Voltage Reference 0.6V', 'kicadSymbolki_description': '0.6V 25μA Micropower Voltage Reference, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : ISL21070DIH306Z-TK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

