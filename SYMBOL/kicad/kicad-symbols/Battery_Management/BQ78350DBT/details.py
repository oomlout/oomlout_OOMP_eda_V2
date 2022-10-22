
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ78350DBT"
    hexID = "SZKBATMANAGEMENTBQ7835DBT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ78350DBT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-30_4.4x7.8mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq78350.pdf', 'kicadSymbolki_keywords': 'battery, management, Li-Ion, Gauge, controller', 'kicadSymbolki_description': 'Lithium battery fuel gauge, battery management controller for BQ769x0, TSSOP-30', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.5mm*'}])
    newPart['name'].append('BQ78350DBT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

