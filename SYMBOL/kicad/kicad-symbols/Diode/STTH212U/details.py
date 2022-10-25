
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STTH212U"
    hexID = "SZKDIODESTTH212U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'S2JTR', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STTH212U', 'kicadSymbolFootprint': 'Diode_SMD:D_SMB', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stth212.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '1200V 2A High Voltage Ultrafast Diode, SMB', 'kicadSymbolki_fp_filters': '*D?SMB*'}])
    newPart['name'].append('Diode : STTH212U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

