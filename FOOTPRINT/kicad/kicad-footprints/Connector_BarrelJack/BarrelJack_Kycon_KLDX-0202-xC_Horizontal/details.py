
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_Kycon_KLDX-0202-xC_Horizontal"
    hexID = "FZKCNBARRELJBARRELJKYCONKLDX22XCHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_Kycon_KLDX-0202-xC_Horizontal', 'description': 'DC Barrel Jack 2mm or 2.5mm center pin, https://www.kycon.com/Pub_Eng_Draw/KLDX-0202-AC%20&%20BC.pdf', 'tags': 'power jack 2mm 2.5mm KLDX-0202-BC KLDX-0202-AC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_Kycon_KLDX-0202-xC_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_Kycon_KLDX-0202-xC_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

