
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SG-105F"
    hexID = "SZKSENPROXIMITYSG15F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SG-105F', 'kicadSymbolFootprint': 'OptoDevice:Kodenshi_SG105F', 'kicadSymbolDatasheet': 'http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105F.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor, DIP-lie THT-package', 'kicadSymbolki_fp_filters': 'Kodenshi*SG105F*'}])
    newPart['name'].append('Sensor_Proximity : SG-105F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

