
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MCV_1,5_11-G-3.81_1x11_P3.81mm_Vertical"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMCV1511G3811X11P381VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_11-G-3.81_1x11_P3.81mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/11-G-3.81; number of pins: 11; pin pitch: 3.81mm; Vertical || order number: 1803510 8A 160V', 'tags': 'phoenix_contact connector MCV_01x11_G_3.81mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MCV_1,5_11-G-3.81_1x11_P3.81mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MCV_1,5_11-G-3.81_1x11_P3.81mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

