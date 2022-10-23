
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7946"
    hexID = "SZKTRANSISTORFETIRF7946"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB008NE2LX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7946', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MX', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7946pbf.pdf?fileId=5546d462533600a40153560cc0a41d43', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '198A Id, 40V Vds, 1.4mOhm Rds, N-Channel MOSFET, DirectFET MX', 'kicadSymbolki_fp_filters': 'DirectFET*MX*'}])
    newPart['name'].append('IRF7946')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

