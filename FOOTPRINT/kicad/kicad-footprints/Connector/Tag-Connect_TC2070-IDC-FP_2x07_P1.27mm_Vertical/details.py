
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "Tag-Connect_TC2070-IDC-FP_2x07_P1.27mm_Vertical"
    hexID = "FZKCNTAGCONNECTTC27IDCFP2X7P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Tag-Connect_TC2070-IDC-FP_2x07_P1.27mm_Vertical', 'description': 'Tag-Connect programming header; http://www.tag-connect.com/Materials/TC2070-IDC%20Datasheet.pdf', 'tags': 'tag connect programming header pogo pins', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector : Tag-Connect_TC2070-IDC-FP_2x07_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

