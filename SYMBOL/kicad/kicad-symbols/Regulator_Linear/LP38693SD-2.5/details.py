
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38693SD-2.5"
    hexID = "SZKREGULATORLINEARLP38693SD25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP38693SD-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38693SD-2.5', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_3x3mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lp38693.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '500-mA Low-Dropout CMOS Linear Regulators Stable With Ceramic Output Capacitors, 2.5V output voltage, Enable Pin, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x3mm*P0.95mm*'}])
    newPart['name'].append('LP38693SD-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

