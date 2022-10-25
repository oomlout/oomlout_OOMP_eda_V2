
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMS8050ET30"
    hexID = "SZKTRANSISTORFETFDMS85ET3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMS8050ET30', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMS8050ET30-D.pdf', 'kicadSymbolki_keywords': 'powertrench MOSFET fairchild', 'kicadSymbolki_description': '55A Id, 30V Vds, N-Channel PowerTrench MOSFET, 0.65mOhm Ron, 285nC Qgmax, -55 to 175 °C, 5x6mm SON8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : FDMS8050ET30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

