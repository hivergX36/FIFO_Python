import re
class fifo:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def push(self, item):
        if len(self.queue) >= self.size:
            self.queue.pop(0)  # Remove the oldest item
        self.queue.append(item)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)  # Remove and return the oldest item

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    def parsing_checknumber(self,lignes,indice,caracter:str):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != caracter and lignes[indice][compteur2] != caracter):
              while(lignes[indice][compteur2] != caracter):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def parse_data(self, text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        data = [self.parsing_checknumber(lines, i,",") for i in range(len(lines))]
        self.queue = [data[i][j] for i in range(1, len(data)) for j in range(0, len(data[i]))]
        self.size = len(self.queue)
