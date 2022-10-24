
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Converter"
    oIndex = "Balun_Johanson_0896BM15A0001"
    hexID = "FZKRFBALUNJOHANSON896BM15A1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Balun_Johanson_0896BM15A0001', 'description': 'https://www.johansontechnology.com/datasheets/0896BM15A0001/0896BM15A0001.pdf', 'tags': 'balun RF', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Converter.3dshapes/Balun_Johanson_0896BM15A0001.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Converter : Balun_Johanson_0896BM15A0001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

