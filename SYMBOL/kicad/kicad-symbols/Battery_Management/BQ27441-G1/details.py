
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ27441-G1"
    hexID = "SZKBATMANAGEMENTBQ27441G1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ27441-G1', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PDSO-N12', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq27441-g1.pdf', 'kicadSymbolki_keywords': 'Fuel Gauge', 'kicadSymbolki_description': 'System Side Li Ion/Polymer Fuel Gauge, PDSON-12', 'kicadSymbolki_fp_filters': '*PDSO*N12*'}])
    newPart['name'].append('BQ27441-G1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

