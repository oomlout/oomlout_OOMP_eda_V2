
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH480"
    hexID = "SZKLSFH48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH482', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH480', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-2_Window', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic1/00083613_0.pdf', 'kicadSymbolki_keywords': 'IR LED Opto', 'kicadSymbolki_description': 'GaAlAs Infrared LED (880 nm), TO-18 package', 'kicadSymbolki_fp_filters': 'TO?18*Window*'}])
    newPart['name'].append('LED : SFH480')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

