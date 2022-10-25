
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "ISD2560S"
    hexID = "SZKAUDIOISD256S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISD2560S', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheetspdf.com/pdf-file/700027/Winbond/ISD2560/1', 'kicadSymbolki_keywords': 'isd2560', 'kicadSymbolki_description': 'Single-Chip Voice Record/Playback Device 60-Second Duration, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('Audio : ISD2560S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

