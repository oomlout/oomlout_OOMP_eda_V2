
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT1634CCZ-5"
    hexID = "SZKREFERENCEVOLTAGELT1634CCZ5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1634CCZ-1.25', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1634CCZ-5', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1634ff.pdf', 'kicadSymbolki_keywords': 'voltage reference Micropower', 'kicadSymbolki_description': '5V Micropower Precision Shunt Voltage Reference, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Reference_Voltage : LT1634CCZ-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

