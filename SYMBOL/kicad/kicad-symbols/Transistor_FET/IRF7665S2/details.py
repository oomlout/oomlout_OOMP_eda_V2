
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7665S2"
    hexID = "SZKTRANSISTORFETIRF7665S2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7665S2', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SB', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7665s2pbf.pdf?fileId=5546d462533600a401535603d3ba1c86', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '14.4A Id, 100V Vds, 62mOhm Rds, N-Channel MOSFET, DirectFET SB', 'kicadSymbolki_fp_filters': 'DirectFET*SB*'}])
    newPart['name'].append('Transistor_FET : IRF7665S2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

