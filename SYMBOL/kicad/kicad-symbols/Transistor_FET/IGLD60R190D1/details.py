
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGLD60R190D1"
    hexID = "SZKTRANSISTORFETIGLD6R19D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IGLD60R070D1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGLD60R190D1', 'kicadSymbolFootprint': 'Package_SON:Infineon_PG-LSON-8-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGLD60R190D1-DataSheet-v02_00-EN.pdf?fileId=5546d46269e1c019016a6d78ff5e2aba', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '10A Id, 600V Vds, 190mOhm, N-Channel GaN MOSFET, LSON-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*LSON*1*'}])
    newPart['name'].append('Transistor_FET : IGLD60R190D1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

