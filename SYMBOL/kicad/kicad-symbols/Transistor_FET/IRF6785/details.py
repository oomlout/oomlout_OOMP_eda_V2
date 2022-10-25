
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6785"
    hexID = "SZKTRANSISTORFETIRF6785"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB165N15NZ3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6785', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MZ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6785mpbf.pdf?fileId=5546d462533600a4015355ed8cc31aa2', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '19A Id, 200V Vds, 100mOhm Rds, N-Channel MOSFET, DirectFET MZ', 'kicadSymbolki_fp_filters': 'DirectFET*MZ*'}])
    newPart['name'].append('Transistor_FET : IRF6785')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

