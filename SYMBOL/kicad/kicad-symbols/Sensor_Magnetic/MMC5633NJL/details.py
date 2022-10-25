
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "MMC5633NJL"
    hexID = "SZKSENMAGNETICC5633NJL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MMC5633NJL', 'kicadSymbolFootprint': 'Package_BGA:WLP-4_0.86x0.86mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.memsic.com/uploadfiles/2020/08/20200827165106864.pdf', 'kicadSymbolki_keywords': 'I2C I3C magnetic 3-axis sensor magnetometer AMR magnetoresistance', 'kicadSymbolki_description': '3-axis AMR Magnetometer, 30 G, I2C & I3C  Interface, 2mG RMS, WLP-4', 'kicadSymbolki_fp_filters': 'WLP*0.86x0.86mm?P0.4mm*'}])
    newPart['name'].append('Sensor_Magnetic : MMC5633NJL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

