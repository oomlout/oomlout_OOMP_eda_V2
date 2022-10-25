
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AZ1117-2.5"
    hexID = "SZKREGULATORLINEARAZ111725"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AZ1117-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AZ1117-2.5', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AZ1117.pdf', 'kicadSymbolki_keywords': 'Fixed Voltage Regulator 1A Positive LDO', 'kicadSymbolki_description': '1A 20V Fixed LDO Linear Regulator, 2.5V, SOT-89/SOT-223/TO-220/TO-252/TO-263', 'kicadSymbolki_fp_filters': 'SOT?223* SOT?89* TO?220* TO?252* TO?263*'}])
    newPart['name'].append('Regulator_Linear : AZ1117-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

