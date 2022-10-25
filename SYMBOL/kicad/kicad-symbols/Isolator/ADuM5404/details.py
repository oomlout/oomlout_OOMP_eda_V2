
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM5404"
    hexID = "SZKISOLATORADUM544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM5404', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM5401_5402_5403_5404.pdf', 'kicadSymbolki_keywords': 'digital isolator galvanic isopower', 'kicadSymbolki_description': 'Quad-Channel 2.5kV isolator with integrated isoPower dc-dc converter, 0 Input / 4 output, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Isolator : ADuM5404')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

