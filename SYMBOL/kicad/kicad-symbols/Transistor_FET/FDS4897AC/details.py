
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDS4897AC"
    hexID = "SZKTRANSISTORFETFDS4897AC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7309IPBF', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDS4897AC', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDS4897AC-D.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel P-Channel MOSFET', 'kicadSymbolki_description': '6.1A Id, 40V Vds, Dual N and P Channel MOSFET, 26mOhm Ron, 10V Vgs, SO8L', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Transistor_FET : FDS4897AC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

