
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "ISD2575P"
    hexID = "SZKAUDIOISD2575P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ISD2560P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISD2575P', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'https://datasheetspdf.com/pdf-file/700027/Winbond/ISD2560/1', 'kicadSymbolki_keywords': 'isd2575', 'kicadSymbolki_description': 'Single-Chip Voice Record/Playback Device 75-Second Duration, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Audio : ISD2575P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

