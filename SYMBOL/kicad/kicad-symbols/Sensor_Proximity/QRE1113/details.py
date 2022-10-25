
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "QRE1113"
    hexID = "SZKSENPROXIMITYQRE1113"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'QRE1113', 'kicadSymbolFootprint': 'OptoDevice:OnSemi_CASE100AQ', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/QRE1113-D.PDF', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto reflex coupler', 'kicadSymbolki_description': 'Miniature Reflective Optical Object Sensor, DIP-like THT-package', 'kicadSymbolki_fp_filters': 'OnSemi*CASE100AQ*'}])
    newPart['name'].append('Sensor_Proximity : QRE1113')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

