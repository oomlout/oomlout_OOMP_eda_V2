
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB_Micro_B_Female_Vert_1051330001"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUMBFEMALEVERT151331"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro_B_Female_Vert_1051330001', 'description': 'http://www.molex.com/pdm_docs/sd/1051330001_sd.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('digikey-footprints : USB_Micro_B_Female_Vert_1051330001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

