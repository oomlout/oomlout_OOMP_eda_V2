
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "MN3007"
    hexID = "SZKAUDIOMN37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MN3007', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.experimentalistsanonymous.com/diy/Datasheets/MN3007.pdf', 'kicadSymbolki_keywords': 'Matsushita Panasonic BBD', 'kicadSymbolki_description': '1024-STAGE LOW NOISE BBD (bucket brigade device), delay time 5.12ms to 51.2ms, S/N 80dB, clock frequency range 10KHz to 100KHz', 'kicadSymbolki_fp_filters': 'DIP-8*'}])
    newPart['name'].append('Audio : MN3007')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

