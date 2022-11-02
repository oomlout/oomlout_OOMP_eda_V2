
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-sullinselectronics"
    oIndex = "050_610_HF-30_60"
    hexID = "FZECONSULLINSELECTRONICS561HF36"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-sullinselectronics : 050_610_HF-30_60')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

