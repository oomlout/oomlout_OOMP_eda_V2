
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX1873REEE"
    hexID = "SZKBATMANAGEMENTMAX1873REEE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1873REEE', 'kicadSymbolFootprint': 'Package_SO:QSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1873.pdf', 'kicadSymbolki_keywords': 'Charger for 2 lithium-ion (Li+), 5/6 NickelCadium (NiCD) cells or 5/6 NickelMetalHydride (NiMH), 9 to 28V VDD, -40 to +85 degree Celsius, QSOP-16', 'kicadSymbolki_description': 'Charger for 2 lithium-ion (Li+), 5/6 NickelCadium (NiCD) cells or 5/6 NickelMetalHydride (NiMH), 9 to 28V VDD, -40 to +85 degree Celsius, QSOP-16', 'kicadSymbolki_fp_filters': 'QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('Battery_Management : MAX1873REEE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

