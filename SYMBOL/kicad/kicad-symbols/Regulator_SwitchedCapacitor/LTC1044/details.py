
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LTC1044"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLTC144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1044', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/lt1044.pdf', 'kicadSymbolki_keywords': 'monolithic CMOS switched capacitor voltage converter invert double divide multiply boost', 'kicadSymbolki_description': 'Switched Capacitor Voltage Converter, 1.5V to 9V supply operation, 200uA Max No Load Supply Current at 5V, DIP-8/TO-99', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* TO?99*'}])
    newPart['name'].append('LTC1044')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

