
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF02Z"
    hexID = "SZKREFERENCEVOLTAGEREF2Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF02AP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF02Z', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/REF01_02_03.pdf', 'kicadSymbolki_keywords': 'Precision Voltage Reference 5V', 'kicadSymbolki_description': '5V ±25mV Precision Voltage Reference, CERDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Reference_Voltage : REF02Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

