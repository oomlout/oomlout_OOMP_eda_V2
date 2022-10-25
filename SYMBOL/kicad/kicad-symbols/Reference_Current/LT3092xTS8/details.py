
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Current"
    oIndex = "LT3092xTS8"
    hexID = "SZKREFERENCECURRENTLT392XTS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3092xTS8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-8', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3092fc.pdf', 'kicadSymbolki_keywords': 'current source', 'kicadSymbolki_description': '200mA 2-Terminal Programmable Current Source, TSOT-23-8', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Reference_Current : LT3092xTS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

