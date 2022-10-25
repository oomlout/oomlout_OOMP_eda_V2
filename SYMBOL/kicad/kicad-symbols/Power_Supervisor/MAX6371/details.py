
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MAX6371"
    hexID = "SZKPOWERSUPERVISORMAX6371"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX6369', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX6371', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-8', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX6369-MAX6374.pdf', 'kicadSymbolki_keywords': 'watchdog supervisor', 'kicadSymbolki_description': 'Precision Pin-Selectable Watchdog Timer, 200us to 60s, SOT-23-8', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Supervisor : MAX6371')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

