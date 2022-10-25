
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Jumper"
    oIndex = "SolderJumper_3_Open"
    hexID = "SZKJSOLDERJ3OPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'JP', 'kicadSymbolValue': 'SolderJumper_3_Open', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Solder Jumper SPDT', 'kicadSymbolki_description': 'Solder Jumper, 3-pole, open', 'kicadSymbolki_fp_filters': 'SolderJumper*Open*'}])
    newPart['name'].append('Jumper : SolderJumper_3_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

