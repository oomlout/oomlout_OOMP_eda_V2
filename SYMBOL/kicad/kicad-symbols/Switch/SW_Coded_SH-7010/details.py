
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Coded_SH-7010"
    hexID = "SZKSWITCHSWCODEDSH71"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Coded_SH-7010', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf', 'kicadSymbolki_keywords': 'rotary bcd Real', 'kicadSymbolki_description': 'Rotary switch, 4-bit encoding, 10 positions, Real code', 'kicadSymbolki_fp_filters': 'Nidec*Copal*SH*7010*'}])
    newPart['name'].append('Switch : SW_Coded_SH-7010')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

