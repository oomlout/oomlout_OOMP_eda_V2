
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "SD_Hirose_DM1AA_SF_PEJ82"
    hexID = "FZKCNCARDSDHIROSEDM1AASFPEJ82"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SD_Hirose_DM1AA_SF_PEJ82', 'description': 'SD, SMD, top-mount, push-push (https://www.hirose.com/product/document?clcode=CL0609-0004-8-82&productname=DM1AA-SF-PEJ(82)&series=DM1&documenttype=2DDrawing&lang=en&documentid=0000915301)', 'tags': 'SD card connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/SD_Hirose_DM1AA_SF_PEJ82.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Card : SD_Hirose_DM1AA_SF_PEJ82')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

