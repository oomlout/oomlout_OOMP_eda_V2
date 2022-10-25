
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6614"
    hexID = "SZKTRANSISTORFETIRF6614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF450NE7NH3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6614', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ST', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6614pbf.pdf?fileId=5546d462533600a4015355e8346c1a0f', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '12.7A Id, 40V Vds, 8.3mOhm Rds, N-Channel MOSFET, DirectFET ST', 'kicadSymbolki_fp_filters': 'DirectFET*ST*'}])
    newPart['name'].append('Transistor_FET : IRF6614')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

