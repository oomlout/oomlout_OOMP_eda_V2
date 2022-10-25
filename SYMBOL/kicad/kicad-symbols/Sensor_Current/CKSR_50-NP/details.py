
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CKSR_50-NP"
    hexID = "SZKSENCURRENTCKSR5NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CKSR_15-NP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CKSR_50-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_CKSR', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/cksr_series.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 50A, Unipolar, 0-5V Output', 'kicadSymbolki_fp_filters': 'LEM*CKSR*'}])
    newPart['name'].append('Sensor_Current : CKSR_50-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

