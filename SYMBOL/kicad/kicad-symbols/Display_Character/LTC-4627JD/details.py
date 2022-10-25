
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "LTC-4627JD"
    hexID = "SZKDICHARACTERLTC4627JD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC-4627JG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC-4627JD', 'kicadSymbolFootprint': 'Display_7Segment:LTC-4627Jx', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS30-2001-093/LTC-4627JD.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': '4 digit 7 segment hyper red, common anode', 'kicadSymbolki_fp_filters': 'LTC?4627J*'}])
    newPart['name'].append('Display_Character : LTC-4627JD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

