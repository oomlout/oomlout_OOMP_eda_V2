
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Laser"
    oIndex = "PL450B"
    hexID = "SZKDIODELASERPL45B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'PL450B', 'kicadSymbolFootprint': 'OptoDevice:LaserDiode_TO38ICut-3', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic5/00193831_0.pdf/PL%20450B.pdf', 'kicadSymbolki_keywords': 'opto laserdiode', 'kicadSymbolki_description': 'Blue Laser Diode (450nm), TO-38', 'kicadSymbolki_fp_filters': 'LaserDiode*TO38ICut*'}])
    newPart['name'].append('Diode_Laser : PL450B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

