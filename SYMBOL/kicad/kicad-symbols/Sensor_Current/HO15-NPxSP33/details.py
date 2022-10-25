
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "HO15-NPxSP33"
    hexID = "SZKSENCURRENTHO15NPXSP33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HO8-NPxSP33', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HO15-NPxSP33', 'kicadSymbolFootprint': 'Sensor_Current:LEM_HO8-NP', 'kicadSymbolDatasheet': 'https://www.lem.com/sites/default/files/products_datasheets/ho-np_sp33-1000_series.pdf', 'kicadSymbolki_keywords': 'current transducer', 'kicadSymbolki_description': 'Current Transducer, 15A, Unipolar, 3.3V', 'kicadSymbolki_fp_filters': 'LEM*HO8*NP*'}])
    newPart['name'].append('Sensor_Current : HO15-NPxSP33')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

