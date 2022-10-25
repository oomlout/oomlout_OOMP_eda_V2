
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4365xTS8"
    hexID = "SZKPOWERMANAGEMENTLTC4365XTS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4365xTS8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-8', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4365fa.pdf', 'kicadSymbolki_keywords': 'overvoltage undervoltage reverse-polarity protection', 'kicadSymbolki_description': 'Overvoltage, Undervoltage and Reverse Supply Protection Controller, 50Hz/60Hz noise rejection, TSOT-23-8', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Power_Management : LTC4365xTS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

