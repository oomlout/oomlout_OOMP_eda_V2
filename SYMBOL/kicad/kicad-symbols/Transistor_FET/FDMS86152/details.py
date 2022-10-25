
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMS86152"
    hexID = "SZKTRANSISTORFETFDMS86152"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMS86152', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'https://www.mouser.fr/datasheet/2/308/FDMS86152-D-1808412.pdf', 'kicadSymbolki_keywords': 'powertrench MOSFET fairchild', 'kicadSymbolki_description': '14A Id, 100V Vds, N-Channel PowerTrench MOSFET, 6mOhm Ron, 50nC Qgmax, -55 to 150 °C, 5x6mm SON8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : FDMS86152')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

