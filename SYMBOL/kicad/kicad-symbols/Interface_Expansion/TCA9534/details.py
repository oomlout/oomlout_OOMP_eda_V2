
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9534"
    hexID = "SZKINTERFACEEXPANSIONTCA9534"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9534', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9534.pdf', 'kicadSymbolki_keywords': 'SMBUS I2C Expander', 'kicadSymbolki_description': '8 Bit Port/Expander, I2C SMBUS, Interrupt output, TSSOP-16, SOIC-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm* SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('TCA9534')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

