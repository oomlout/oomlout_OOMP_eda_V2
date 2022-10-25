
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HO25-NP"
    hexID = "SZKSENCURRENTHO25NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HO8-NP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HO25-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HO8-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/ho-np-0000_series.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 25A, Unipolar, 5V', 'kicadSymbolki_fp_filters': 'LEM*HO8*NP*'}])
    newPart['name'].append('Sensor_Current : HO25-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

