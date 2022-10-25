
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "CDNBS08-SLVU2.8-4"
    hexID = "SZKPOWERPROTECTIONCDNBS8SLVU284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CDNBS08-SLVU2.8-4', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.bourns.com/pdfs/CDNBS08-SLVU28-4.pdf', 'kicadSymbolki_keywords': 'ESD protection suppression transient', 'kicadSymbolki_description': 'Quad bidirectional transil, Suppressor for ESD protection, 5V Standoff, 4 Channels, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Protection : CDNBS08-SLVU2.8-4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

