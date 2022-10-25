
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "RFShield_TwoPieces"
    hexID = "SZKDEVICERFSHTWOPIECES"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RFShield_TwoPieces', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'RF EMI shielding cabinet', 'kicadSymbolki_description': 'Two-piece EMI RF shielding cabinet'}])
    newPart['name'].append('Device : RFShield_TwoPieces')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

