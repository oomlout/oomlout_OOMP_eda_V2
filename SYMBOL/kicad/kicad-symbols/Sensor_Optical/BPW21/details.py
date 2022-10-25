
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPW21"
    hexID = "SZKSENOPTICALBPW21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BPW21', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-5-2_Window', 'kicadSymbolDatasheet': 'http://techwww.in.tu-clausthal.de/site/Dokumentation/Dioden/Fotodioden/BPW21-Fotodiode.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon Photodiode for the visible spectral range, TO-5 package', 'kicadSymbolki_fp_filters': 'TO?5*Window*'}])
    newPart['name'].append('Sensor_Optical : BPW21')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

