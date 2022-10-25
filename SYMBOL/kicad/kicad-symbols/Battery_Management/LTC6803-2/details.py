
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC6803-2"
    hexID = "SZKBATMANAGEMENTLTC6832"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6803-2', 'kicadSymbolFootprint': 'Package_SO:SSOP-44_5.3x12.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/680324fa.pdf', 'kicadSymbolki_keywords': 'battery balance afe', 'kicadSymbolki_description': 'Multicell Battery Stack Monitor, 12-cell max, multi-chemistry, integrated balancing, stackable, serial interface', 'kicadSymbolki_fp_filters': 'SSOP*5.3x12.8mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : LTC6803-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

