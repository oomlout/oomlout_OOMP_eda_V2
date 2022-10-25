
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "NOA1305"
    hexID = "SZKSENOPTICALNOA135"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NOA1305', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NOA1305-D.PDF', 'kicadSymbolki_keywords': 'opto ambient light sensor', 'kicadSymbolki_description': 'Ambient Light Sensor with I2C Interface and Dark Current Compensation', 'kicadSymbolki_fp_filters': 'DFN*6*P0.65mm*'}])
    newPart['name'].append('Sensor_Optical : NOA1305')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

