
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP184xSE"
    hexID = "SZKISOLATORTLP184XSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP184', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP184xSE', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-4_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=14118&prodName=TLP184(SE', 'kicadSymbolki_keywords': 'NPN AC DC Optocoupler', 'kicadSymbolki_description': 'AC/DC Optocoupler, Vce 80V, CTR 50-100%, MFSOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP184xSE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

