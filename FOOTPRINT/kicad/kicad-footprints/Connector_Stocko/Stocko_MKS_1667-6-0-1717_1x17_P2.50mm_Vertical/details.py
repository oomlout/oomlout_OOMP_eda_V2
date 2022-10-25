
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Stocko"
    oIndex = "Stocko_MKS_1667-6-0-1717_1x17_P2.50mm_Vertical"
    hexID = "FZKCNSTOCKOSTOCKOMKS1667617171X17P25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Stocko_MKS_1667-6-0-1717_1x17_P2.50mm_Vertical', 'description': 'Stocko MKS 16xx series connector, (https://www.stocko-contact.com/downloads/steckverbindersystem-raster-2,5-mm.pdf#page=15), generated with kicad-footprint-generator', 'tags': 'Stocko RFK MKS 16xx', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Stocko.3dshapes/Stocko_MKS_1667-6-0-1717_1x17_P2.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Stocko : Stocko_MKS_1667-6-0-1717_1x17_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

