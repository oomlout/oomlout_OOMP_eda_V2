
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-357T"
    hexID = "SZKISOLATORLTV357T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTV-356T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-357T', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x3.6mm_P2.54mm', 'kicadSymbolDatasheet': 'https://www.buerklin.com/medias/sys_master/download/download/h91/ha0/8892020588574.pdf', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 35V, CTR 50%, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x3.6mm*P2.54mm*'}])
    newPart['name'].append('Isolator : LTV-357T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

