
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LT1054xSW"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLT154XSW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1054xSW', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1054lfh.pdf', 'kicadSymbolki_keywords': 'monolithic bipolar switched capacitor voltage converter regulator inverter doubler shutdown', 'kicadSymbolki_description': 'Switched-Capacitor Voltage Converter with Regulator, output current 100mA, operating range 3.5V to 15V, low loss 1.1V at 100mA, SO-16', 'kicadSymbolki_fp_filters': 'SOIC?16W*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('LT1054xSW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

