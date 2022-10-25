
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "Tag-Connect_TC2050-IDC-NL_2x05_P1.27mm_Vertical_with_bottom_clip"
    hexID = "FZKCNTAGCONNECTTC25IDCNL2X5P127VERTICALWITHBOTTOMCLIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Tag-Connect_TC2050-IDC-NL_2x05_P1.27mm_Vertical_with_bottom_clip', 'description': 'Tag-Connect programming header with bottom courtyard for TC2050-NL Clip board ; https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/TC2050-IDC-NL_Datasheet_8.pdf https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/TC2050-CLIP_Datasheet_25.pdf', 'tags': 'tag connect programming header pogo pins', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector : Tag-Connect_TC2050-IDC-NL_2x05_P1.27mm_Vertical_with_bottom_clip')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

