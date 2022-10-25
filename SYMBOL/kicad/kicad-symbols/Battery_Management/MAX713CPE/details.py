
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX713CPE"
    hexID = "SZKBATMANAGEMENTMAX713CPE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX712CPE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX713CPE', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX712-MAX713.pdf', 'kicadSymbolki_keywords': 'Fast-charge Nickel Cadmium (NiCd) from a DC source, 0 to +70 Degree Celsius, PDIP-16', 'kicadSymbolki_description': 'Fast-charge Nickel Cadmium (NiCd) from a DC source, 0 to +70 Degree Celsius, PDIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Battery_Management : MAX713CPE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

