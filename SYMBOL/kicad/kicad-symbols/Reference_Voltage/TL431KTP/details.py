
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "TL431KTP"
    hexID = "SZKREFERENCEVOLTAGETL431KTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL431KTP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.jameco.com/Jameco/Products/ProdDS/760499.pdf', 'kicadSymbolki_keywords': 'diode device shunt regulator', 'kicadSymbolki_description': 'Shunt Regulator, TO-252', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('Reference_Voltage : TL431KTP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

