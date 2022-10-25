
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_PJ31060-I_Horizontal"
    hexID = "FZKCNAUDIOJ35PJ316IHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_PJ31060-I_Horizontal', 'description': 'PJ31060-I 6pin SMD 3.5mm headphones jack (http://www.china-bsun.com/Product48/1577.html)', 'tags': 'headphones jack plug stereo 3.5mm PJ31060-I PJ31060', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_PJ31060-I_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_PJ31060-I_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

