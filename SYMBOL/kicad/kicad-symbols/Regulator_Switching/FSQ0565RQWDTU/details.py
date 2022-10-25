
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSQ0565RQWDTU"
    hexID = "SZKREGULATORSWITCHINGFSQ565RQWDTU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FSQ0565RSWDTU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSQ0565RQWDTU', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:Fairchild_TO-220F-6L', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FSQ0565RS-D.PDF', 'kicadSymbolki_keywords': 'Quasi Resonant SMPS Controller 80W AC-DC', 'kicadSymbolki_description': '67kHz Quasi Resonant SMPS Controller w/ Soft Start, max. 80W AC-DC, TO-220F-6L', 'kicadSymbolki_fp_filters': 'Fairchild*TO*220F*6L*'}])
    newPart['name'].append('Regulator_Switching : FSQ0565RQWDTU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

