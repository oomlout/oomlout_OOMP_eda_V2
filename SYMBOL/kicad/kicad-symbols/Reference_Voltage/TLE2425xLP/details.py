
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "TLE2425xLP"
    hexID = "SZKREFERENCEVOLTAGETLE2425XLP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLE2426xLP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLE2425xLP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tle2425.pdf', 'kicadSymbolki_keywords': 'Rail splitter precision virtual ground 2.5V', 'kicadSymbolki_description': 'Precision virtual ground, 2.5V output, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Reference_Voltage : TLE2425xLP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

