
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "BMM150"
    hexID = "SZKSENMAGNETICB15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BMM150', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-12_1.56x1.56mm_P0.4mm', 'kicadSymbolDatasheet': 'https://www.mouser.com/datasheet/2/783/BST-BMM150-DS001-01-786480.pdf', 'kicadSymbolki_keywords': 'BOSH Geomagnetic Sensor', 'kicadSymbolki_description': 'Geomagnetic Sensor, WLCSP-12', 'kicadSymbolki_fp_filters': 'WLCSP*1.56x1.56mm*P0.4mm*'}])
    newPart['name'].append('Sensor_Magnetic : BMM150')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

