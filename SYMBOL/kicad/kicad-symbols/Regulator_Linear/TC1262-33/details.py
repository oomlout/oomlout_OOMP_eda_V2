
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TC1262-33"
    hexID = "SZKREGULATORLINEARTC126233"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC1262-33', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21373C.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 3.3V 500mA Positive CMOS LDO Microchip', 'kicadSymbolki_description': '500mA Low Dropout CMOS Voltage Regulator, Fixed Output 3.3V, TO-220/SOT-223/TO-263', 'kicadSymbolki_fp_filters': 'SOT?223* TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : TC1262-33')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

