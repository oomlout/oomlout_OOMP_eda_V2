
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB104N08NP3"
    hexID = "SZKTRANSISTORFETBSB14N8NP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB104N08NP3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MP', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB104N08NP3_G-DS-v02_01-en.pdf?fileId=db3a304341e0aed00141efc548ca1b2b', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '50A Id, 80V Vds, 10.4mOhm Rds, N-Channel MOSFET, DirectFET MP', 'kicadSymbolki_fp_filters': 'DirectFET*MP*'}])
    newPart['name'].append('BSB104N08NP3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

