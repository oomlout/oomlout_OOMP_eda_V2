
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT1790-4.096"
    hexID = "SZKREFERENCEVOLTAGELT179496"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1790-1.25', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1790-4.096', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1790fc.pdf', 'kicadSymbolki_keywords': 'voltage reference Micropower', 'kicadSymbolki_description': '4.096V Voltage Reference, Low Dropout, Micropower, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23?6*'}])
    newPart['name'].append('Reference_Voltage : LT1790-4.096')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

