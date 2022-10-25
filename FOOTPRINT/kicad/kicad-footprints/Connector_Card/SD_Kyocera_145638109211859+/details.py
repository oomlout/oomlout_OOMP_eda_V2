
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "SD_Kyocera_145638109211859+"
    hexID = "FZKCNCARDSDKYOCERA14563819211859+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SD_Kyocera_145638109211859+', 'description': 'SD Card Connector, Reverse Type, Outer Tail, Without Ejector (https://global.kyocera.com/prdct/electro/product/pdf/5638.pdf)', 'tags': 'sd card smt', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/SD_Kyocera_145638109211859+.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Card : SD_Kyocera_145638109211859+')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

