
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6710S2"
    hexID = "SZKTRANSISTORFETIRF671S2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6710S2', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_S1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6710s2pbf.pdf?fileId=5546d462533600a4015355ece3db1a78', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '12A Id, 25V Vds, 5.9mOhm Rds, N-Channel MOSFET, DirectFET S1', 'kicadSymbolki_fp_filters': 'DirectFET*S1*'}])
    newPart['name'].append('IRF6710S2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

