
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGT60R190D1S"
    hexID = "SZKTRANSISTORFETIGT6R19D1S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IGT60R070D1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGT60R190D1S', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HSOF-8-3_ThermalVias', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGT60R190D1S-DataSheet-v03_01-EN.pdf?fileId=5546d46265f064ff016685fa29796520', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '12.5A Id, 600V Vds, 190mOhm, N-Channel GaN MOSFET, HSOF-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*HSOF*3*'}])
    newPart['name'].append('Transistor_FET : IGT60R190D1S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

