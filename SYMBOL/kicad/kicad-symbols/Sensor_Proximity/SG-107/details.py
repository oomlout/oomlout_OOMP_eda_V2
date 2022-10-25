
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SG-107"
    hexID = "SZKSENPROXIMITYSG17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-105', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SG-107', 'kicadSymbolFootprint': 'OptoDevice:Kodenshi_SG105', 'kicadSymbolDatasheet': 'http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-107.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor, SMD-package with PCB-cutout', 'kicadSymbolki_fp_filters': 'Kodenshi*SG105*'}])
    newPart['name'].append('Sensor_Proximity : SG-107')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

