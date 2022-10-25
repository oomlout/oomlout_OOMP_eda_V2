
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "Tag-Connect_TC2050-IDC-FP_2x05_P1.27mm_Vertical"
    hexID = "FZKCNTAGCONNECTTC25IDCFP2X5P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Tag-Connect_TC2050-IDC-FP_2x05_P1.27mm_Vertical', 'description': 'Tag-Connect programming header; http://www.tag-connect.com/Materials/TC2050-IDC-430%20Datasheet.pdf', 'tags': 'tag connect programming header pogo pins', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector : Tag-Connect_TC2050-IDC-FP_2x05_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

