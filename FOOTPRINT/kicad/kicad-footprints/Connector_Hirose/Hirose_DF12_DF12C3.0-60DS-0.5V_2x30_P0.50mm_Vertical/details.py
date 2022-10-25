
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF12_DF12C3.0-60DS-0.5V_2x30_P0.50mm_Vertical"
    hexID = "FZKCNHIROSEHIROSEDF12DF12C36DS5V2X3P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF12_DF12C3.0-60DS-0.5V_2x30_P0.50mm_Vertical', 'description': 'Hirose DF12C SMD, DF12C3.0-60DS-0.5V, 60 Pins per row (https://www.hirose.com/product/document?clcode=CL0537-0694-9-81&productname=DF12C(3.0)-50DS-0.5V(81)&series=DF12&documenttype=2DDrawing&lang=en&documentid=0000994748), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF12 vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF12_DF12C3.0-60DS-0.5V_2x30_P0.50mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF12_DF12C3.0-60DS-0.5V_2x30_P0.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

