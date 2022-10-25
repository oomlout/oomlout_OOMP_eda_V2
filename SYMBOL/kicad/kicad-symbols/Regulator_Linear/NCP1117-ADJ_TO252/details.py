
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP1117-ADJ_TO252"
    hexID = "SZKREGULATORLINEARNCP1117ADJTO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1117-ADJ_TO252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF', 'kicadSymbolki_keywords': 'REGULATOR LDO ADJUSTABLE', 'kicadSymbolki_description': '1A Low drop-out regulator, Adjustable Output 1.25 - 18.8V, TO-252 (DPAK)', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : NCP1117-ADJ_TO252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

