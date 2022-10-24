
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Converter"
    oIndex = "Anaren_0805_2012Metric-6"
    hexID = "FZKRFANAREN85212METRIC6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Anaren_0805_2012Metric-6', 'description': 'https://cdn.anaren.com/product-documents/Xinger/DirectionalCouplers/DC4759J5020AHF/DC4759J5020AHF_DataSheet(Rev_E).pdf', 'tags': 'coupler rf', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Converter.3dshapes/Anaren_0805_2012Metric-6.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Converter : Anaren_0805_2012Metric-6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

