
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP2768A"
    hexID = "SZKISOLATORTLP2768A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP2768A', 'kicadSymbolFootprint': 'Package_SO:SO-6L_10x3.84mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=36717&prodName=TLP2768A', 'kicadSymbolki_keywords': 'Photocouple highspeed inverting open collector output', 'kicadSymbolki_description': '20-Mbps high speed inverting photocouple,5 kVrms, 2.7 - 5.5 Vdd, open collector, SO-6L', 'kicadSymbolki_fp_filters': 'SO*6L*10x3.84mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP2768A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

