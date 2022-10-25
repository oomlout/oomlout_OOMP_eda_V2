
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LT1054"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLT154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1054', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1054lfh.pdf', 'kicadSymbolki_keywords': 'monolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'kicadSymbolki_description': 'Switched-Capacitor Voltage Converter with Regulator, output current 100mA, operating range 3.5V to 15V, low loss 1.1V at 100mA, DIP-8/SO-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : LT1054')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

