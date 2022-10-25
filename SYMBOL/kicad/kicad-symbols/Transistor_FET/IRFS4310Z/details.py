
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFS4310Z"
    hexID = "SZKTRANSISTORFETIRFS431Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STB15N80K5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFS4310Z', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfb4310zpbf.pdf?fileId=5546d462533600a4015356161b4d1e2d', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '120A Id, 100V Vds, 4.8mOhm Rds, N-Channel HEXFET Power MOSFET, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Transistor_FET : IRFS4310Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

