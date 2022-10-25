
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB-C_Female_Vert_DX07S024WJ3R400"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUCFEMALEVERTDX7S24WJ3R4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB-C_Female_Vert_DX07S024WJ3R400', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : USB-C_Female_Vert_DX07S024WJ3R400')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

