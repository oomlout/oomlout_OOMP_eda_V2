
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MASWSS0178"
    hexID = "SZKRFSWITCHMASWSS178"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MASWSS0178', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias', 'kicadSymbolDatasheet': 'https://cdn.macom.com/datasheets/MASWSS0178.pdf', 'kicadSymbolki_keywords': 'RF switch SPDT', 'kicadSymbolki_description': 'SPDT High Isolation Terminated Switch, 0.01-3.0 GHz, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('RF_Switch : MASWSS0178')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

