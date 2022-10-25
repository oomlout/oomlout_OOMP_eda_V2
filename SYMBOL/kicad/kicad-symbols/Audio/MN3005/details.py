
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "MN3005"
    hexID = "SZKAUDIOMN35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MN3005', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.experimentalistsanonymous.com/diy/Datasheets/MN3005.pdf', 'kicadSymbolki_keywords': 'Matsushita Panasonic BBD', 'kicadSymbolki_description': '4096-STAGE LONG DELAY BBD (bucket brigade device), delay time 20.48ms to 204.8ms, S/N 75dB, clock frequency range 10KHz to 100KHz', 'kicadSymbolki_fp_filters': 'DIP-8*'}])
    newPart['name'].append('Audio : MN3005')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

