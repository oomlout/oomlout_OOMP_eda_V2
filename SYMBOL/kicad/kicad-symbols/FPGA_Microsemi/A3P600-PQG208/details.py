
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Microsemi"
    oIndex = "A3P600-PQG208"
    hexID = "SZKFPGAMSEMIA3P6PQG28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A3P600-PQG208', 'kicadSymbolFootprint': 'Package_QFP:PQFP-208_28x28mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.microsemi.com/document-portal/doc_download/130704-proasic3-flash-family-fpgas-datasheet', 'kicadSymbolki_keywords': 'ProASIC3 ACTEL FLASH', 'kicadSymbolki_description': 'Actel ProASIC3 Flash Family FPGAs, 600k Gates, 208pin QFP', 'kicadSymbolki_fp_filters': '*PQFP*28x28mm*P0.5mm*'}])
    newPart['name'].append('A3P600-PQG208')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

