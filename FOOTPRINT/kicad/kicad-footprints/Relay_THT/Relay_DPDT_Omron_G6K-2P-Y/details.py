
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPDT_Omron_G6K-2P-Y"
    hexID = "FZKRELRELAYDPDTOMRONG6K2PY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Omron_G6K-2P-Y', 'description': 'Omron G6K-2P-Y relay package http://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k.pdf', 'tags': 'Omron G6K-2P-Y relay', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Omron_G6K-2P-Y.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_DPDT_Omron_G6K-2P-Y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

