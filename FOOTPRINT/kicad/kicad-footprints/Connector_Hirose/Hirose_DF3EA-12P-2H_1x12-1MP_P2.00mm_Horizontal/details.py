
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF3EA-12P-2H_1x12-1MP_P2.00mm_Horizontal"
    hexID = "FZKCNHIROSEHIROSEDF3EA12P2H1X121MPP2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF3EA-12P-2H_1x12-1MP_P2.00mm_Horizontal', 'description': 'Hirose  series connector, DF3EA-12P-2H (https://www.hirose.com/product/document?clcode=CL0543-0332-0-51&productname=DF3EA-5P-2H(51)&series=DF3&documenttype=2DDrawing&lang=en&documentid=0001163317), generated with kicad-footprint-generator', 'tags': 'connector Hirose  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF3EA-12P-2H_1x12-1MP_P2.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF3EA-12P-2H_1x12-1MP_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

