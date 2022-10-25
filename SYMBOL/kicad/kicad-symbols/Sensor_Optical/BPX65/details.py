
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPX65"
    hexID = "SZKSENOPTICALBPX65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BPX65', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-2_Lens', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic1/00181579_0.pdf/BPX%2065,%20Lead%20(Pb)%20Free%20Product%20-%20RoHS%20Compliant.pdf', 'kicadSymbolki_keywords': 'opto PIN photo diode', 'kicadSymbolki_description': 'Silicon PIN Photodiode, TO-18 package', 'kicadSymbolki_fp_filters': 'TO?18*Lens*'}])
    newPart['name'].append('Sensor_Optical : BPX65')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

