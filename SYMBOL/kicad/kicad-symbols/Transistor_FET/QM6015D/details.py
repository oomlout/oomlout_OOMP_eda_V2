
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "QM6015D"
    hexID = "SZKTRANSISTORFETQM615D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'QM6015D', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.jaolen.com/images/pdf/QM6015D.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-35A Id, -60V Vds, P-Channel Power MOSFET, 25mOhm Ron, 25.0nC Qg (typ), TO252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Transistor_FET : QM6015D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

