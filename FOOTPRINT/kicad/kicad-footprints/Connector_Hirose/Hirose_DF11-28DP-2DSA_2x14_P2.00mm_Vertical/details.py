
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF11-28DP-2DSA_2x14_P2.00mm_Vertical"
    hexID = "FZKCNHIROSEHIROSEDF1128DP2DSA2X14P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF11-28DP-2DSA_2x14_P2.00mm_Vertical', 'description': 'Hirose DF11 through hole, DF11-28DP-2DSA, 14 Pins per row (https://www.hirose.com/product/document?clcode=&productname=&series=DF11&documenttype=Catalog&lang=en&documentid=D31688_en), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF11 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF11-28DP-2DSA_2x14_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF11-28DP-2DSA_2x14_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

