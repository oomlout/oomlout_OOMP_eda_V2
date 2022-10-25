
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGT60R070D1"
    hexID = "SZKTRANSISTORFETIGT6R7D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGT60R070D1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HSOF-8-3_ThermalVias', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGT60R070D1-DataSheet-v02_01-EN.pdf?fileId=5546d46265f064ff016686028dd56526', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '31A Id, 600V Vds, 70mOhm, N-Channel GaN MOSFET, HSOF-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*HSOF*3*'}])
    newPart['name'].append('Transistor_FET : IGT60R070D1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

