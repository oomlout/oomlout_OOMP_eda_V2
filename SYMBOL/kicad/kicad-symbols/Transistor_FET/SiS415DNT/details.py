
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SiS415DNT"
    hexID = "SZKTRANSISTORFETSIS415DNT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SiS415DNT', 'kicadSymbolFootprint': 'Package_SO:Vishay_PowerPAK_1212-8_Single', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/63684/sis415dnt.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-35A Id, -20V Vds, P-Channel MOSFET, PowerPAK 1212-8 Single', 'kicadSymbolki_fp_filters': 'Vishay*PowerPAK*1212*Single*'}])
    newPart['name'].append('Transistor_FET : SiS415DNT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

