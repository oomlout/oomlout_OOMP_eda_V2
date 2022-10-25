
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_BM24_BM24-40DS-2-0.35V_2x20_P0.35mm_PowerPin2_Vertical"
    hexID = "FZKCNHIROSEHIROSEBM24BM244DS235V2X2P35POWERPIN2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_BM24_BM24-40DS-2-0.35V_2x20_P0.35mm_PowerPin2_Vertical', 'description': 'Hirose BM24 series connector, BM24-40DS/2-0.35V (https://www.hirose.com/product/en/download_file/key_name/BM24/category/Catalog/doc_file_id/47680/?file_category_id=4&item_id=50&is_series=1)', 'tags': 'connector Hirose 40pin receptacle vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_BM24_BM24-40DS-2-0.35V_2x20_P0.35mm_PowerPin2_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Hirose : Hirose_BM24_BM24-40DS-2-0.35V_2x20_P0.35mm_PowerPin2_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

