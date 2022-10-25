
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRLB8721PBF"
    hexID = "SZKTRANSISTORFETIRLB8721PBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRLB8721PBF', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/irlb8721pbf.pdf?fileId=5546d462533600a40153566056732591', 'kicadSymbolki_keywords': 'N-Channel HEXFET MOSFET Logic-Level', 'kicadSymbolki_description': '62A Id, 30V Vds, 8.7 mOhm Rds, N-Channel HEXFET Power MOSFET, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : IRLB8721PBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

