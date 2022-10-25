
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4370xMS"
    hexID = "SZKPOWERMANAGEMENTLTC437XMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4370xMS', 'kicadSymbolFootprint': 'Package_SO:MSOP-16_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4370f.pdf', 'kicadSymbolki_keywords': 'ideal-diode or-ing current sharing load balancing', 'kicadSymbolki_description': 'OR Controller Current Sharing Controller N-Channel 2:1, MSOP-16', 'kicadSymbolki_fp_filters': 'MSOP*3x4mm*P0.5mm*'}])
    newPart['name'].append('Power_Management : LTC4370xMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

