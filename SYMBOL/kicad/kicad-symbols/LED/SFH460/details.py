
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH460"
    hexID = "SZKLSFH46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH460', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-2_Window', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic6/00029609_0.pdf/SFh%20460.pdf', 'kicadSymbolki_keywords': 'opto IR LED', 'kicadSymbolki_description': 'GaAlAs Infrared LED, TO-18 package', 'kicadSymbolki_fp_filters': 'TO?18*Window*'}])
    newPart['name'].append('LED : SFH460')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

