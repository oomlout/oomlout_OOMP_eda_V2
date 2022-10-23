
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Buzzer_Murata_PKMCS0909E"
    hexID = "FZKBZBUZZERMPKMCS99E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Buzzer_Murata_PKMCS0909E', 'description': 'Murata Buzzer http://www.murata.com/en-us/api/pdfdownloadapi?cate=&partno=PKMCS0909E4000-R1', 'tags': 'Murata Buzzer Beeper', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Buzzer_Murata_PKMCS0909E.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Buzzer_Murata_PKMCS0909E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

