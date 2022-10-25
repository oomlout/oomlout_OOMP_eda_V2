
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SUD50P04-08"
    hexID = "SZKTRANSISTORFETSUD5P48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SUD19P06-60', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SUD50P04-08', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/65594/sud50p04-08.pdf', 'kicadSymbolki_keywords': 'TrenchFET P-Channel Power MOSFET', 'kicadSymbolki_description': '50A Id, 40V Vds, TrenchFET P-Channel Power MOSFET, 8.1mOhm Ron, 159nC Qg, -55 to 150 °C, TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : SUD50P04-08')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

