
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D5.0mm-4_RGB_Staggered_Pins"
    hexID = "FZKLLD54RGBSTAGGEREDPINS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D5.0mm-4_RGB_Staggered_Pins', 'description': 'LED, diameter 5.0mm, 4 pins, WP154A4, https://www.kingbright.com/attachments/file/psearch/000/00/00/L-154A4SUREQBFZGEW(Ver.11A).pdf', 'tags': 'rgb led', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D5.0mm-4_RGB_Staggered_Pins.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('LED_THT : LED_D5.0mm-4_RGB_Staggered_Pins')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

