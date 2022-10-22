
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "LGA-12_9x9mm_LSM303C"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSLGA129X9LSM33C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-12_9x9mm_LSM303C', 'description': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/59/aa/fb/3b/85/9e/4e/0a/DM00089896.pdf/files/DM00089896.pdf/jcr:content/translations/en.DM00089896.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : LGA-12_9x9mm_LSM303C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

