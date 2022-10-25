
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "FODM217A"
    hexID = "SZKISOLATORFODM217A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FODM217A', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FODM214-D.PDF', 'kicadSymbolki_keywords': 'DC Phototransistor Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 80V, CTR 80-160%, SOP-4', 'kicadSymbolki_fp_filters': 'SOP*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : FODM217A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

