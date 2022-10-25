
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "US1K"
    hexID = "SZKDIODEUS1K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MRA4003T3G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'US1K', 'kicadSymbolFootprint': 'Diode_SMD:D_SMA', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/ds16008.pdf', 'kicadSymbolki_keywords': 'Ultra Fast', 'kicadSymbolki_description': '800V, 1A, General Purpose Rectifier Diode, SMA(DO-214AC)', 'kicadSymbolki_fp_filters': 'D*SMA*'}])
    newPart['name'].append('Diode : US1K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

