
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "TE_PCH-1xxx2M"
    hexID = "SZKRELAYTEPCH1XXX2M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'TE_PCH-1xxx2M', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_TE_PCH-1xxx2M', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FPCH_series_relay_data_sheet_E%7F1215%7Fpdf%7FEnglish%7FENG_DS_PCH_series_relay_data_sheet_E_1215.pdf%7F9-1440003-0', 'kicadSymbolki_keywords': 'Miniature Single Pole Relay', 'kicadSymbolki_description': 'TE PCH relay, Miniature Single Pole, SPST-NO', 'kicadSymbolki_fp_filters': 'Relay*SPST*TE*PCH*1***2M*'}])
    newPart['name'].append('Relay : TE_PCH-1xxx2M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

