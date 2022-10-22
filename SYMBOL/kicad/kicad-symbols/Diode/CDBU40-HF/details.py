
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "CDBU40-HF"
    hexID = "SZKDIODECDBU4HF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B120-E3', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CDBU40-HF', 'kicadSymbolFootprint': 'Diode_SMD:D_0603_1608Metric', 'kicadSymbolDatasheet': 'https://www.comchiptech.com/admin/files/product/QW-G1012-CDBU40-HF-RevA321692.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '40V 200mA Schottky Barrier Rectifier Diode, 0603', 'kicadSymbolki_fp_filters': 'D*0603*'}])
    newPart['name'].append('CDBU40-HF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

