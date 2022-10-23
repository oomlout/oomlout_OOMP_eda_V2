
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7483M"
    hexID = "SZKTRANSISTORFETIRF7483M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF40DM229', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7483M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MF', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7483mpbf.pdf?fileId=5546d462533600a4015355ff98011c32', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '135A Id, 40V Vds, 2.3mOhm Rds, N-Channel MOSFET, DirectFET MF', 'kicadSymbolki_fp_filters': 'DirectFET*MF*'}])
    newPart['name'].append('IRF7483M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

