
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "DRV5055A2xLPGxQ1"
    hexID = "SZKSENMAGNETICDRV555A2XLPGXQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DRV5055A1xLPGxQ1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV5055A2xLPGxQ1', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/drv5055-q1.pdf', 'kicadSymbolki_keywords': 'Automotive Ratiometric Linear Hall Effect Sensor AEC-Q100', 'kicadSymbolki_description': '50 mV/mT,±42-mT, 20-kHz, 3.3/5V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('DRV5055A2xLPGxQ1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

