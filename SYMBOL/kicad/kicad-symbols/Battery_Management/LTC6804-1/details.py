
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC6804-1"
    hexID = "SZKBATMANAGEMENTLTC6841"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6804-1', 'kicadSymbolFootprint': 'Package_SO:SSOP-48_5.3x12.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/680412fc.pdf', 'kicadSymbolki_keywords': 'battery balance afe', 'kicadSymbolki_description': 'Multicell Battery Stack Monitor, 12-cell max, multi-chemistry, integrated balancing, stackable, serial interface, SSOP-48', 'kicadSymbolki_fp_filters': 'SSOP*5.3x12.8mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : LTC6804-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

