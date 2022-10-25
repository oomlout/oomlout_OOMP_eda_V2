
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LT1641-2"
    hexID = "SZKPOWERMANAGEMENTLT16412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1641-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1641-2', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/164112fc.pdf', 'kicadSymbolki_keywords': 'high-voltage hot-swap', 'kicadSymbolki_description': 'High voltage hot swap controller, +9V to +80V operation, with auto-retry feature', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : LT1641-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

