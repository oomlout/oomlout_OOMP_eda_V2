
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "VTL5C"
    hexID = "SZKISOLATORVTL5C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VTL5C', 'kicadSymbolFootprint': 'OptoDevice:PerkinElmer_VTL5C', 'kicadSymbolDatasheet': 'http://www.qsl.net/wa1ion/vactrol/vactrol.pdf', 'kicadSymbolki_keywords': 'vactrol', 'kicadSymbolki_description': 'Low Cost Axial Vactrols', 'kicadSymbolki_fp_filters': 'PerkinElmer*VTL5C*'}])
    newPart['name'].append('Isolator : VTL5C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

