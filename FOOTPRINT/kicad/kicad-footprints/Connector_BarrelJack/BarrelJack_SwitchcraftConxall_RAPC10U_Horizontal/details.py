
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_SwitchcraftConxall_RAPC10U_Horizontal"
    hexID = "FZKCNBARRELJBARRELJSWITCHCRAFTCONXALLRAPC1UHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_SwitchcraftConxall_RAPC10U_Horizontal', 'description': 'DC Power Jack, 13A, 24V, Panel Mount,Through-hole, https://www.switchcraft.com/Drawings/RAPC10U_CD.pdf', 'tags': 'barreljack switchcraftconxall dc power', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_SwitchcraftConxall_RAPC10U_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_SwitchcraftConxall_RAPC10U_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

