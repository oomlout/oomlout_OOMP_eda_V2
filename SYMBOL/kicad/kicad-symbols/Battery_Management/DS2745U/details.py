
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "DS2745U"
    hexID = "SZKBATMANAGEMENTDS2745U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS2745U', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS2745.pdf', 'kicadSymbolki_keywords': 'Current-flow, voltage and temperature  measurement to support batterycapacity monitoring, 2.5V to 4.5V VDD, -40 to +85 degree Celsius, TSSOP-8', 'kicadSymbolki_description': 'Current-flow, voltage and temperature  measurement to support batterycapacity monitoring, 2.5V to 4.5V VDD, -40 to +85 degree Celsius, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Battery_Management : DS2745U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

