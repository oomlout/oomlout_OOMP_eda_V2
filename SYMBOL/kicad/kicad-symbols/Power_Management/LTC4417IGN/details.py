
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4417IGN"
    hexID = "SZKPOWERMANAGEMENTLTC4417IGN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4417CGN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4417IGN', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4417f.pdf', 'kicadSymbolki_keywords': 'switch power FET sequence', 'kicadSymbolki_description': 'Prioritized PowerPath Controller, Selects Highest Priority Supply from Three Inputs, –40°C to 85°C, SSOP', 'kicadSymbolki_fp_filters': 'SSOP-24*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Power_Management : LTC4417IGN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

