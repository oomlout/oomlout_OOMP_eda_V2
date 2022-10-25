
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-355T"
    hexID = "SZKISOLATORLTV355T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-355T', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x3.6mm_P2.54mm', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS70-2001-006/S_110_LTV-355T%2020140520.pdf', 'kicadSymbolki_keywords': 'NPN Darlington DC Optocoupler', 'kicadSymbolki_description': 'DC Darlington Optocoupler, Vce 35V, CTR 600%, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x3.6mm*P2.54mm*'}])
    newPart['name'].append('Isolator : LTV-355T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

