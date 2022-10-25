
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRLML6402"
    hexID = "SZKTRANSISTORFETIRLML642"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TP0610T', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRLML6402', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irlml6402pbf.pdf?fileId=5546d462533600a401535668d5c2263c', 'kicadSymbolki_keywords': 'P-Channel HEXFET MOSFET', 'kicadSymbolki_description': '-3.7A Id, -20V Vds, 65mOhm Rds, P-Channel HEXFET Power MOSFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : IRLML6402')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

