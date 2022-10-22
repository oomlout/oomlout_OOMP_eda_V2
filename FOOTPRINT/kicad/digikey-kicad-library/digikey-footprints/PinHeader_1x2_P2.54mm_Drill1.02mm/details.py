
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "PinHeader_1x2_P2.54mm_Drill1.02mm"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSPINHEADER1X2P254DRILL12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x2_P2.54mm_Drill1.02mm', 'description': 'http://www.molex.com/pdm_docs/sd/022232031_sd.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : PinHeader_1x2_P2.54mm_Drill1.02mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

