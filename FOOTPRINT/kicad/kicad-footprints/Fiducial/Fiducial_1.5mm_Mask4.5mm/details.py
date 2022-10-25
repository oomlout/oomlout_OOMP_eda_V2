
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fiducial"
    oIndex = "Fiducial_1.5mm_Mask4.5mm"
    hexID = "FZKFIDFID15MASK45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fiducial_1.5mm_Mask4.5mm', 'description': 'Circular Fiducial, 1.5mm bare copper, 4.5mm soldermask opening', 'tags': 'fiducial', 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Fiducial : Fiducial_1.5mm_Mask4.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

