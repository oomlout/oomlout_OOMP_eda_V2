
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "TLV493D"
    hexID = "SZKSENMAGNETICTLV493D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV493D', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-TLV493D-A1B6-DS-v01_00-EN.pdf?fileId=5546d462525dbac40152a6b85c760e80', 'kicadSymbolki_keywords': 'magnetic field i2c', 'kicadSymbolki_description': 'Low power 3D magnetic sensor, I2C interface, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Sensor_Magnetic : TLV493D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

