
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24090DGQ"
    hexID = "SZKBATMANAGEMENTBQ249DGQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24090DGQ', 'kicadSymbolFootprint': 'Package_SO:HVSSOP-10-1EP_3x3mm_P0.5mm_EP1.57x1.88mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24090.pdf', 'kicadSymbolki_keywords': 'battery charger singlecell li-ion li-poly, 1A', 'kicadSymbolki_description': '1A, Single-Input, SingleCell Li-Ion and Li-Pol BatteryCharger, HVSSOP-10', 'kicadSymbolki_fp_filters': 'HVSSOP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : BQ24090DGQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

