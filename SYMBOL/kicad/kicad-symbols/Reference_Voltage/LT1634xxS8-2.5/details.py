
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT1634xxS8-2.5"
    hexID = "SZKREFERENCEVOLTAGELT1634XXS825"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1634xxS8-1.25', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1634xxS8-2.5', 'kicadSymbolFootprint': 'Package_SO:SO-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1634ff.pdf', 'kicadSymbolki_keywords': 'voltage reference Micropower', 'kicadSymbolki_description': '2.5V Micropower Precision Shunt Voltage Reference, SO-8', 'kicadSymbolki_fp_filters': 'SO?8*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : LT1634xxS8-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

