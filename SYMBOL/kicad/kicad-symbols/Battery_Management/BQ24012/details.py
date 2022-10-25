
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24012"
    hexID = "SZKBATMANAGEMENTBQ2412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24012', 'kicadSymbolFootprint': 'Package_SON:VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24012.pdf', 'kicadSymbolki_keywords': 'Batter, Charger, Li-Ion', 'kicadSymbolki_description': 'Single-Chip Li-Ion Charge Management IC, DFN-10', 'kicadSymbolki_fp_filters': 'VSON*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : BQ24012')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

