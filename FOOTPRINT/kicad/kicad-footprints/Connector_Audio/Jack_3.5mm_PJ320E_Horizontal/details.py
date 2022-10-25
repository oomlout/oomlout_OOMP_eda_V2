
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_PJ320E_Horizontal"
    hexID = "FZKCNAUDIOJ35PJ32EHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_PJ320E_Horizontal', 'description': 'Headphones with microphone connector, 3.5mm, 4 pins (http://www.qingpu-electronics.com/en/products/WQP-PJ320E-177.html)', 'tags': '3.5mm jack mic microphone phones headphones 4pins audio plug', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_PJ320E_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_PJ320E_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

