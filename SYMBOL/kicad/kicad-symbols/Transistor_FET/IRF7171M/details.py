
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7171M"
    hexID = "SZKTRANSISTORFETIRF7171M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB028N06NN3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7171M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MN', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7171mpbf.pdf?fileId=5546d462533600a4015355f1326f1ad6', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '93A Id, 100V Vds, 6.5mOhm Rds, N-Channel MOSFET, DirectFET MN', 'kicadSymbolki_fp_filters': 'DirectFET*MN*'}])
    newPart['name'].append('Transistor_FET : IRF7171M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

