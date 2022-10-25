
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP2770"
    hexID = "SZKISOLATORTLP277"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP2770', 'kicadSymbolFootprint': 'Package_SO:SO-6L_10x3.84mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=53548&prodName=TLP2770', 'kicadSymbolki_keywords': 'Photocouple highspeed non inverting push-pull output', 'kicadSymbolki_description': '20-Mbps low-power non inverting photocouple,5 kVrms, 2.7 to 5.5 Vdd, push-pull output, SO-6L', 'kicadSymbolki_fp_filters': 'SO*6L*10x3.84mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP2770')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

