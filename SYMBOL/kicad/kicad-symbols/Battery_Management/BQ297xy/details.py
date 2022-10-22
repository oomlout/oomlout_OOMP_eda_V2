
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ297xy"
    hexID = "SZKBATMANAGEMENTBQ297XY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ297xy', 'kicadSymbolFootprint': 'Package_SON:WSON-6_1.5x1.5mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq2970.pdf', 'kicadSymbolki_keywords': 'protection Li-Ion Li-Pol', 'kicadSymbolki_description': 'Voltage and Current Protection for Single-Cell Li-Ion and Li-Polymer Batteries', 'kicadSymbolki_fp_filters': 'WSON*1.5x1.5mm*P0.5mm*'}])
    newPart['name'].append('BQ297xy')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

