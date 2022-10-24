
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Kodenshi_SG105F"
    hexID = "FZKOPKODENSHISG15F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Kodenshi_SG105F', 'description': 'package for Kodenshi SG-105F, see http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105F.pdf', 'tags': 'refective opto couple photo coupler', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kodenshi_SG105F.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Kodenshi_SG105F')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

