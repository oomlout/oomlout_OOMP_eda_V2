
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "FODM214A"
    hexID = "SZKISOLATORFODM214A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FODM214', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FODM214A', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FODM214-D.PDF', 'kicadSymbolki_keywords': 'AC DC Phototransistor Optocoupler', 'kicadSymbolki_description': 'AC/DC Optocoupler, Vce 80V, CTR 50-250%, SOP-4', 'kicadSymbolki_fp_filters': 'SOP*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('FODM214A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

