
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2987-3.3_SOIC8_VSSOP8"
    hexID = "SZKREGULATORLINEARLP298733SOIC8VSS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP2987-5.0_SOIC8_VSSOP8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2987-3.3_SOIC8_VSSOP8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2987.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator 200mA 5V', 'kicadSymbolki_description': '200mA Linear LDO Regulator, MicroPower, Fixed Output 3.3V, SO8/MSOP8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('LP2987-3.3_SOIC8_VSSOP8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

