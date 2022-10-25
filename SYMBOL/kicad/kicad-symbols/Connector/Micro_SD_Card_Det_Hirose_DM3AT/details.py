
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Micro_SD_Card_Det_Hirose_DM3AT"
    hexID = "SZKCNMSDCARDDETHIROSEDM3AT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Micro_SD_Card_Det', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Micro_SD_Card_Det_Hirose_DM3AT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.hirose.com/product/en/download_file/key_name/DM3/category/Catalog/doc_file_id/49662/?file_category_id=4&item_id=195&is_series=1', 'kicadSymbolki_keywords': 'connector SD microsd', 'kicadSymbolki_description': 'Micro SD Card Socket with card detection pins', 'kicadSymbolki_fp_filters': 'microSD*'}])
    newPart['name'].append('Connector : Micro_SD_Card_Det_Hirose_DM3AT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

