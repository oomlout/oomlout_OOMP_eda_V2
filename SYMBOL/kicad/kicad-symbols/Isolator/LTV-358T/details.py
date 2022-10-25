
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-358T"
    hexID = "SZKISOLATORLTV358T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTV-356T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-358T', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x3.6mm_P2.54mm', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS70-2001-022/S_110_LTV-358T%2020140520.pdf', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 120V, CTR 50%, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x3.6mm*P2.54mm*'}])
    newPart['name'].append('Isolator : LTV-358T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

