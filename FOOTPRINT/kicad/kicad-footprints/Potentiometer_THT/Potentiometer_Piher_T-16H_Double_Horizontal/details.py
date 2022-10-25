
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Piher_T-16H_Double_Horizontal"
    hexID = "FZKPPOTENTIOMETERPIHERT16HDOUBLEHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Piher_T-16H_Double_Horizontal', 'description': 'Potentiometer, horizontal, Piher T-16H Double, http://www.piher-nacesa.com/pdf/22-T16v03.pdf', 'tags': 'Potentiometer horizontal Piher T-16H Double', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Piher_T-16H_Double_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Piher_T-16H_Double_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

