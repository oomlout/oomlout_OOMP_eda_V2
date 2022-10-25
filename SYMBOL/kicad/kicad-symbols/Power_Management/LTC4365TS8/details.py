
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4365TS8"
    hexID = "SZKPOWERMANAGEMENTLTC4365TS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4365TS8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4365fa.pdf', 'kicadSymbolki_keywords': 'overvoltage undervoltage reverse-polarity protection', 'kicadSymbolki_description': 'Overvoltage, Undervoltage and Reverse Supply Protection Controller, TSOT23-8 package, 50Hz/60Hz noise rejection', 'kicadSymbolki_fp_filters': '*SOT?23*'}])
    newPart['name'].append('Power_Management : LTC4365TS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

