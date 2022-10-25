
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SUD19P06-60"
    hexID = "SZKTRANSISTORFETSUD19P66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SUD19P06-60', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/69253/sud19p06.pdf', 'kicadSymbolki_keywords': 'TrenchFET P-Channel Power MOSFET', 'kicadSymbolki_description': '19A Id, 60V Vds, TrenchFET P-Channel Power MOSFET, 60mOhm Ron, 40nC Qg, -55 to 150 °C, TO-252-2', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : SUD19P06-60')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

