
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AZ1084-5.0"
    hexID = "SZKREGULATORLINEARAZ1845"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AZ1084-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AZ1084-5.0', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AZ1084.pdf', 'kicadSymbolki_keywords': 'Fixed Voltage Regulator 5A Positive LDO', 'kicadSymbolki_description': '5A 12V Fixed LDO Linear Regulator, 1.5V, TO-220/TO-252/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?252* TO?263*'}])
    newPart['name'].append('AZ1084-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

