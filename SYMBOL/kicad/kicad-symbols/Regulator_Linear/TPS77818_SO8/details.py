
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS77818_SO8"
    hexID = "SZKREGULATORLINEARTPS77818SO8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS77815_SO8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS77818_SO8', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps777.pdf', 'kicadSymbolki_keywords': '750mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '750mA Fast-Transient Low Dropout Voltage Regulator, Fixed Output 1.8V, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : TPS77818_SO8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

