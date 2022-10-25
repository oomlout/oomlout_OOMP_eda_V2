
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HO150-NP"
    hexID = "SZKSENCURRENTHO15NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HO40-NP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HO150-NP', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HO40-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/ho-np_0100__1100_series.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 40A, Unipolar, 5V', 'kicadSymbolki_fp_filters': 'LEM*HO40*NP*'}])
    newPart['name'].append('Sensor_Current : HO150-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

