
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SG-107F"
    hexID = "SZKSENPROXIMITYSG17F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SG-105F', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SG-107F', 'kicadSymbolFootprint': 'OptoDevice:Kodenshi_SG105F', 'kicadSymbolDatasheet': 'https://www.pacer.co.uk/Assets/User/1055-SG-107F.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor, DIP-lie THT-package', 'kicadSymbolki_fp_filters': 'Kodenshi*SG105F*'}])
    newPart['name'].append('Sensor_Proximity : SG-107F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

