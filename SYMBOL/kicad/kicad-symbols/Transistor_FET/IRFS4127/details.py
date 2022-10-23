
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFS4127"
    hexID = "SZKTRANSISTORFETIRFS4127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STB15N80K5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFS4127', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfs4127pbf.pdf?fileId=5546d462533600a401535636ee7b2192', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '72A Id, 200V Vds, 18.6mOhm Rds, N-Channel MOSFET, 18.6mOhm Ron, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('IRFS4127')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

