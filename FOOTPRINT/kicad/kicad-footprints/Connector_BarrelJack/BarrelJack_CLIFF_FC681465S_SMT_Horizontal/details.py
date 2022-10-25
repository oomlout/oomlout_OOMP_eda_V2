
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_CLIFF_FC681465S_SMT_Horizontal"
    hexID = "FZKCNBARRELJBARRELJCLIFFFC681465SSHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_CLIFF_FC681465S_SMT_Horizontal', 'description': 'Surface-mount DC Barrel Jack, https://www.cliffuk.co.uk/products/dcconnectors/FC681465S.pdf', 'tags': 'Power Jack SMT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CLIFF_FC681465S_SMT_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_CLIFF_FC681465S_SMT_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

