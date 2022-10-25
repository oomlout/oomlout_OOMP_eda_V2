
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "TLP3123"
    hexID = "SZKRFTLP3123"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP3123', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x3.9mm_P2.54mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=10047&prodName=TLP3123', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'Solid State Relay (Photo MOSFET) 40V, 1A, 0.1Ohm, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x3.9mm*P2.54mm*'}])
    newPart['name'].append('RF : TLP3123')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

