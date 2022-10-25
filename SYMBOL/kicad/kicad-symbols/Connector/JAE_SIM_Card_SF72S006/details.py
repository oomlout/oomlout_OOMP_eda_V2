
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "JAE_SIM_Card_SF72S006"
    hexID = "SZKCNJAESIMCARDSF72S6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'JAE_SIM_Card_SF72S006', 'kicadSymbolFootprint': 'Connector_JAE:JAE_SIM_Card_SF72S006', 'kicadSymbolDatasheet': 'https://www.jae.com/direct/topics/topics_file_download/topics_id=68892&ext_no=06&index=0&_lang=en&v=202003111511468456809', 'kicadSymbolki_keywords': 'SIM card UICC 4FF', 'kicadSymbolki_description': 'Nano-SIM Card (4FF) connector with Detect Switch', 'kicadSymbolki_fp_filters': 'JAE*SIM*Card*SF72S006*'}])
    newPart['name'].append('Connector : JAE_SIM_Card_SF72S006')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

