
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "PT1000"
    hexID = "SZKSENTEMPERATUREPT1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PT100', 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'PT1000', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.heraeus.com/media/media/group/doc_group/products_1/hst/sot_to/de_15/to_92_d.pdf', 'kicadSymbolki_keywords': 'platinum temperature sensor RTD', 'kicadSymbolki_description': 'PT1000 platinum temperature sensor (RTD)', 'kicadSymbolki_fp_filters': 'TO?92* PIN?ARRAY* bornier* Terminal?Block* SOD70* R*1206* R*0805*'}])
    newPart['name'].append('PT1000')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

