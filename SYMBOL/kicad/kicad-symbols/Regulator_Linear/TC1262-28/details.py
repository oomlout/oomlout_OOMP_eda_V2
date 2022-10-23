
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TC1262-28"
    hexID = "SZKREGULATORLINEARTC126228"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TC1262-33', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC1262-28', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21373C.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 2.8V 500mA Positive CMOS LDO Microchip', 'kicadSymbolki_description': '500mA Low Dropout CMOS Voltage Regulator, Fixed Output 2.8V, TO-220/SOT-223/TO-263', 'kicadSymbolki_fp_filters': 'SOT?223* TO?220* TO?263*'}])
    newPart['name'].append('TC1262-28')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

