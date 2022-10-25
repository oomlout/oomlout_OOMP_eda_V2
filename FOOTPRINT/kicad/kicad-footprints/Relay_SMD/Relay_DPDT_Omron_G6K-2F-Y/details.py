
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_DPDT_Omron_G6K-2F-Y"
    hexID = "FZKRELAYSMRELAYDPDTOMRONG6K2FY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_Omron_G6K-2F-Y', 'description': 'Omron G6K-2F-Y relay package http://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k.pdf', 'tags': 'Omron G6K-2F-Y relay', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_DPDT_Omron_G6K-2F-Y.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Relay_SMD : Relay_DPDT_Omron_G6K-2F-Y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

