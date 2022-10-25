
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM317_TO-252"
    hexID = "SZKREGULATORLINEARLM317TO252"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM317_TO-252', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/snvs774n/snvs774n.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Positive', 'kicadSymbolki_description': '1.5A 35V Adjustable Linear Regulator, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : LM317_TO-252')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

