
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "ICL7660"
    hexID = "SZKREGULATORSWITCHEDCAPACITORICL766"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX1044', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICL7660', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/ICL7660-MAX1044.pdf', 'kicadSymbolki_keywords': 'monolithic CMOS switched capacitor voltage converter invert double divide multiply', 'kicadSymbolki_description': 'Switched-Capacitor Voltage Converter, 1.5V to 10.0V operating supply voltage, 10mA with a 0.5V output drop, SO-8/DIP-8/µMAX-8/TO-99', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* MSOP*3x3mm*P0.65mm* TO?99*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : ICL7660')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

