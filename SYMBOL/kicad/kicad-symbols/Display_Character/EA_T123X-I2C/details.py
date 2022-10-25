
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "EA_T123X-I2C"
    hexID = "SZKDICHARACTEREAT123XI2C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_T123X-I2C', 'kicadSymbolFootprint': 'Display:EA_T123X-I2C', 'kicadSymbolDatasheet': 'http://www.lcd-module.de/pdf/doma/t123-i2c.pdf', 'kicadSymbolki_keywords': 'display LCD 7-segment', 'kicadSymbolki_description': '3 Lines, 12 character alpha numeric LCD, transreflective STN and FSTN Gray, I2C, single or dual power', 'kicadSymbolki_fp_filters': 'EA?T123X?I2C*'}])
    newPart['name'].append('Display_Character : EA_T123X-I2C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

