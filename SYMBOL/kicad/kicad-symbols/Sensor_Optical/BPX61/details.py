
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPX61"
    hexID = "SZKSENOPTICALBPX61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BPW21', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BPX61', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-5-2_Window', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic3/00101650_0.pdf', 'kicadSymbolki_keywords': 'photodiode opto', 'kicadSymbolki_description': 'Silicon Photodiode for the visible spectral range', 'kicadSymbolki_fp_filters': 'TO?5*Window*'}])
    newPart['name'].append('Sensor_Optical : BPX61')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

