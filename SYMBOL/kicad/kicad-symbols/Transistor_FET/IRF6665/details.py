
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6665"
    hexID = "SZKTRANSISTORFETIRF6665"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6655', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6665', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SH', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6665pbf.pdf?fileId=5546d462533600a4015355ec8dcb1a62', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '19A Id, 100V Vds, 62mOhm Rds, N-Channel MOSFET, DirectFET SH', 'kicadSymbolki_fp_filters': 'DirectFET*SH*'}])
    newPart['name'].append('IRF6665')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

