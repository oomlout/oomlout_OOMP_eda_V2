
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB-C_Female_12401X"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUCFEMALE1241X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB-C_Female_12401X', 'description': 'https://media.digikey.com/pdf/Data%20Sheets/Amphenol%20PDFs/12401610E4%232A_Dwg.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('digikey-footprints : USB-C_Female_12401X')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

