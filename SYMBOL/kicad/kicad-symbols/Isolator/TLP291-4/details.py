
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP291-4"
    hexID = "SZKISOLATORTLP2914"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP291-4', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_4.55x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=12858&prodName=TLP291-4', 'kicadSymbolki_keywords': 'NPN DC Quad Optocoupler', 'kicadSymbolki_description': 'Quad DC Optocoupler, Vce 80V, CTR 50-100%, SOP16', 'kicadSymbolki_fp_filters': 'SOIC*4.55x10.3mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP291-4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

