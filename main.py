filePath = './data/data.json'

def setDataset(filePath):
    with open (filePath, 'r') as dataset:
        for data in dataset:
            return data
        
if __name__ == "__main__":
    setDataset(filePath)