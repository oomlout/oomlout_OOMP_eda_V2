
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "INA233"
    hexID = "SZKANALOGADCINA233"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA226', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA233', 'kicadSymbolFootprint': 'Package_SO:VSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ina233.pdf', 'kicadSymbolki_keywords': 'ADC I2C 16-Bit Oversampling Current Shunt', 'kicadSymbolki_description': 'High-Side or Low-Side Measurement, Bi-Directional Current and Power Monitor (0-36V) with I2C, SMBus-, and PMBus-Compatible Interface, VSSOP-10', 'kicadSymbolki_fp_filters': 'VSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('INA233')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

