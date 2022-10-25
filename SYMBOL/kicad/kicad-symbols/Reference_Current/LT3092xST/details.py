
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Current"
    oIndex = "LT3092xST"
    hexID = "SZKREFERENCECURRENTLT392XST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3092xST', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3092fc.pdf', 'kicadSymbolki_keywords': 'current source', 'kicadSymbolki_description': '200mA 2-Terminal Programmable Current Source, SOT-223', 'kicadSymbolki_fp_filters': 'SOT*223*TabPin2*'}])
    newPart['name'].append('Reference_Current : LT3092xST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

