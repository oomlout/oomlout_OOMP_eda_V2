
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Laser"
    oIndex = "PLT5_510"
    hexID = "SZKDIODELASERPLT551"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PL450B', 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'PLT5_510', 'kicadSymbolFootprint': 'OptoDevice:LaserDiode_TO38ICut-3', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic2/00227065_0.pdf/PLT5%20510.pdf', 'kicadSymbolki_keywords': 'opto laserdiode', 'kicadSymbolki_description': 'Green Laser Diode (510nm), TO-38', 'kicadSymbolki_fp_filters': 'LaserDiode*TO38ICut*'}])
    newPart['name'].append('PLT5_510')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

