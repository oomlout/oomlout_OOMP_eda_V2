
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Laser"
    oIndex = "PLT5_488"
    hexID = "SZKDIODELASERPLT5488"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'PLT5_488', 'kicadSymbolFootprint': 'OptoDevice:LaserDiode_TO56-3', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic6/00206440_0.pdf/PLT5%20488.pdf', 'kicadSymbolki_keywords': 'opto laserdiode', 'kicadSymbolki_description': 'Cyan Laser Diode (488nm), TO-56', 'kicadSymbolki_fp_filters': 'LaserDiode*TO56*'}])
    newPart['name'].append('Diode_Laser : PLT5_488')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

