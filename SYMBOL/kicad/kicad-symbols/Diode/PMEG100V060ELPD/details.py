
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG100V060ELPD"
    hexID = "SZKDIODEPMEG1V6ELPD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG45A10EPD', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG100V060ELPD', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Nexperia_CFP15_SOT-1289', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG100V060ELPD.pdf', 'kicadSymbolki_keywords': 'ir diode', 'kicadSymbolki_description': '100V, 6A low leakage current MEGA Schottky barrier rectifier, SOT-1289', 'kicadSymbolki_fp_filters': 'Nexperia*CFP15*SOT?1289*'}])
    newPart['name'].append('Diode : PMEG100V060ELPD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

