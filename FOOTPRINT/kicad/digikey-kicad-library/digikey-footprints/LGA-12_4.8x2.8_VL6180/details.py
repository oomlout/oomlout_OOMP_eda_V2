
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "LGA-12_4.8x2.8_VL6180"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSLGA1248X28VL618"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-12_4.8x2.8_VL6180', 'description': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/c4/11/28/86/e6/26/44/b3/DM00112632.pdf/files/DM00112632.pdf/jcr:content/translations/en.DM00112632.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : LGA-12_4.8x2.8_VL6180')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

