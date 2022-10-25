
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_Switronic_ST-005-G_horizontal"
    hexID = "FZKCNAUDIOJ35SWITRONICST5GHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_Switronic_ST-005-G_horizontal', 'description': '3.5mm horizontal headphones jack, http://akizukidenshi.com/download/ds/switronic/ST-005-G.pdf', 'tags': 'Connector Audio Switronic ST-005-G', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_Switronic_ST-005-G_horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_Switronic_ST-005-G_horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

