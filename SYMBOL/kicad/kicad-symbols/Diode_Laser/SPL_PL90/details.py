
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Laser"
    oIndex = "SPL_PL90"
    hexID = "SZKDIODELASERSPLPL9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'SPL_PL90', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic0/00194565_0.pdf/SPL%20PL90.pdf', 'kicadSymbolki_keywords': 'opto laserdiode', 'kicadSymbolki_description': 'Pulsed Laser Diode in Plastic Package 25W Peak Power', 'kicadSymbolki_fp_filters': 'LED*5.0mm*'}])
    newPart['name'].append('Diode_Laser : SPL_PL90')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

