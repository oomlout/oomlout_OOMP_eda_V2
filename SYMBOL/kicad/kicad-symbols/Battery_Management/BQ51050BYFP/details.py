
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ51050BYFP"
    hexID = "SZKBATMANAGEMENTBQ515BYFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ51050BYFP', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq51050b.pdf', 'kicadSymbolki_keywords': 'Qi Wireless Power Receiver Battery Charger 4.2V', 'kicadSymbolki_description': 'Qi v1.2, Wireless Power Receiver and Battery Charger, Vout 4.2V, DSBGA-28', 'kicadSymbolki_fp_filters': 'Texas?DSBGA*1.9x3.0mm*P0.4mm*'}])
    newPart['name'].append('BQ51050BYFP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

