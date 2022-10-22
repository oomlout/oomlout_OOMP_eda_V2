
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HS-40024"
    hexID = "SZKCONHS424"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HS-40003', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HS-40024', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Hahn_HS-400xx_THT', 'kicadSymbolDatasheet': 'https://www.schukat.com/schukat/pdf.nsf/index/17647BA7403E2D39C1257B810041F34E/$file/HS-40024-Serie%20Schemazeichnung-A3%20(1).pdf', 'kicadSymbolki_keywords': '24V 3W AC-DC module power supply', 'kicadSymbolki_description': '24V, 3W, AC-DC module power supply, Hahn', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Hahn*HS*400xx*'}])
    newPart['name'].append('HS-40024')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

