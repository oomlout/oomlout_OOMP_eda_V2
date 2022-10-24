
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Converter"
    oIndex = "Balun_Johanson_0900PC15J0013"
    hexID = "FZKRFBALUNJOHANSON9PC15J13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Balun_Johanson_0900PC15J0013', 'description': 'Johanson 0900PC15J0013 DFN, 10 Pin (https://www.johansontechnology.com/datasheets/0900PC15J0013/0900PC15J0013.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Johanson DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Converter.3dshapes/Balun_Johanson_0900PC15J0013.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('RF_Converter : Balun_Johanson_0900PC15J0013')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

