
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fiducial"
    oIndex = "Fiducial_1mm_Mask2mm"
    hexID = "FZKFIDFID1MASK2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fiducial_1mm_Mask2mm', 'description': 'Circular Fiducial, 1mm bare copper, 2mm soldermask opening (Level A)', 'tags': 'fiducial', 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Fiducial : Fiducial_1mm_Mask2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

