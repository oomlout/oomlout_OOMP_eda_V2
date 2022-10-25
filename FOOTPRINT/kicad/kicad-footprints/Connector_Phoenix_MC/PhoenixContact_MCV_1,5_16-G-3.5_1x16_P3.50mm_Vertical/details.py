
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MCV_1,5_16-G-3.5_1x16_P3.50mm_Vertical"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMCV1516G351X16P35VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_16-G-3.5_1x16_P3.50mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/16-G-3.5; number of pins: 16; pin pitch: 3.50mm; Vertical || order number: 1843745 8A 160V', 'tags': 'phoenix_contact connector MCV_01x16_G_3.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MCV_1,5_16-G-3.5_1x16_P3.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MCV_1,5_16-G-3.5_1x16_P3.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

