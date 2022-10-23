
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF40DM229"
    hexID = "SZKTRANSISTORFETIRF4DM229"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF40DM229', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MF', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRF40DM229-DS-v02_00-EN.pdf?fileId=5546d462557e6e890155a15c899160ea', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '159A Id, 40V Vds, 1.85mOhm Rds, N-Channel MOSFET, DirectFET MF', 'kicadSymbolki_fp_filters': 'DirectFET*MF*'}])
    newPart['name'].append('IRF40DM229')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

