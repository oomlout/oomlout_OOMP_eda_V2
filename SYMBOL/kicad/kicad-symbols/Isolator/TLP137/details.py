
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP137"
    hexID = "SZKISOLATORTLP137"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP137', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-5_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=16744&prodName=TLP137', 'kicadSymbolki_keywords': 'NPN DC Optocoupler Base Connected', 'kicadSymbolki_description': 'DC Optocoupler Base Connected, Vce 80V, CTR 100-200%, MFSOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP137')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

