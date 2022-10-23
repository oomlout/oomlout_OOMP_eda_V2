
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "LTSR25-NP"
    hexID = "SZKSENCURRENTLTSR25NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTSR6-NP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTSR25-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_LTSR-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/ltsr_25-np.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, Unipolar, 25A, 5V supply, DC, AC, pulsed', 'kicadSymbolki_fp_filters': 'LEM*LTSR*NP*'}])
    newPart['name'].append('LTSR25-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

