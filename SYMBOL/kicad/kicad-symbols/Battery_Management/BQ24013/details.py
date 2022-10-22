
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24013"
    hexID = "SZKBATMANAGEMENTBQ2413"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24013', 'kicadSymbolFootprint': 'Package_SON:Texas_DRC0010J_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24012.pdf', 'kicadSymbolki_keywords': 'Batter Charger Li-Ion', 'kicadSymbolki_description': 'Single-Chip Li-Ion Charge Management IC, VSON-10', 'kicadSymbolki_fp_filters': 'Texas*DRC0010J*'}])
    newPart['name'].append('BQ24013')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

