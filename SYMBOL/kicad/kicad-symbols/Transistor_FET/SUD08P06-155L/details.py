
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SUD08P06-155L"
    hexID = "SZKTRANSISTORFETSUD8P6155L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SUD19P06-60', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SUD08P06-155L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/62843/sud08p06-155l-ge3.pdf', 'kicadSymbolki_keywords': 'TrenchFET P-Channel Power MOSFET', 'kicadSymbolki_description': '8.4A Id, 60V Vds, TrenchFET P-Channel Power MOSFET, 155mOhm Ron, 19nC Qg, -55 to 150 °C, TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : SUD08P06-155L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

