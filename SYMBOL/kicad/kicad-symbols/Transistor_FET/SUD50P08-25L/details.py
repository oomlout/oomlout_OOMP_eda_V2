
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SUD50P08-25L"
    hexID = "SZKTRANSISTORFETSUD5P825L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SUD19P06-60', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SUD50P08-25L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/73443/sud50p08.pdf', 'kicadSymbolki_keywords': 'TrenchFET P-Channel Power MOSFET', 'kicadSymbolki_description': '50A Id, 80V Vds, TrenchFET P-Channel Power MOSFET, 25.2mOhm Ron, 160nC Qg, -55 to 175 °C, TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : SUD50P08-25L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

