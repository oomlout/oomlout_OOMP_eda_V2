
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Coded_SH-7080"
    hexID = "SZKSWITCHSWCODEDSH78"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Coded_SH-7080', 'kicadSymbolFootprint': 'Button_Switch_SMD:Nidec_Copal_SH-7040B', 'kicadSymbolDatasheet': 'https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf', 'kicadSymbolki_keywords': 'rotary hex Gray', 'kicadSymbolki_description': 'Rotary switch, 4-bit encoding, 16 positions, Gray code', 'kicadSymbolki_fp_filters': 'Nidec*Copal*SH*7040*'}])
    newPart['name'].append('Switch : SW_Coded_SH-7080')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

