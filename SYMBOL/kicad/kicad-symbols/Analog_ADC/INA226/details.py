
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "INA226"
    hexID = "SZKANALOGADCINA226"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA226', 'kicadSymbolFootprint': 'Package_SO:VSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina226.pdf', 'kicadSymbolki_keywords': 'ADC I2C 16-Bit Oversampling Current Shunt', 'kicadSymbolki_description': 'High-Side or Low-Side Measurement, Bi-Directional Current and Power Monitor (0-36V) with I2C Compatible Interface, VSSOP-10', 'kicadSymbolki_fp_filters': 'VSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('INA226')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

