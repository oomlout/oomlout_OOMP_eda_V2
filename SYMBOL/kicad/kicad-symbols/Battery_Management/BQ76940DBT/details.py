
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ76940DBT"
    hexID = "SZKBATMANAGEMENTBQ7694DBT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ76940DBT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-44_4.4x11.2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq76940.pdf', 'kicadSymbolki_keywords': 'lithium battery balance charge afe', 'kicadSymbolki_description': 'Lithium battery monitor, 9-15 cells, integrated balancing, I2C interface, TSSOP-44', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x11.2mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : BQ76940DBT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

