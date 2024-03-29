from __future__ import print_function
import random
import numpy 
import math

#kromosom/individu di genereate random
def chromosome(p):
    arr=[]
    for i in range (p):
       arr.append(random.randint(0,1)) #randint dibiner agar lebih akurat
    return arr


#populasi = dari kromosom, akan dicari populasinya, ukuran populasi bebas
def population(arrpop,p): 
    pop = []
    for i in range(arrpop):
       pop.append(chromosome(p))
    return pop

#fungsi dari soalnya.
def fungsi(x1,x2): 
    return ((4-(2.1*x1**2)+((x1**4)/3))*(x1**2)+((-4+(4*(x2**2))))*(x2**2))
 

# decode kromosom
def decodeK (krom): 
    list2= list(map(lambda x :2**-x, numpy.arange(1.,(10/2)+1,1)))

    kromx1 = krom[:5] 
    kromx2 = krom[5:]

    x1 = -3+((6)/sum(list2)* sum(list(map(lambda x,y:x*y,kromx1,list2)))) 
    x2 = -2+((4)/sum(list2)* sum(list(map(lambda x,y:x*y,kromx2,list2))))
    
    return x1,x2

#fitnes = nyari nilai terbaik dari fungsi yang diberikan
def fitness(krom):
    x1,x2 = decodeK(krom) 
    return 1/(fungsi(x1,x2)+1) #ditambah 1 untuk menghuindari pembagian dnegan angka 0

#mencari tournament_size dari random populasi
def tournament(population): 
    return population[random.randint(0,len(population)-1)]

def selectParents(c_ind,population):
    best = []
    for i in range(2): 
        for k in range(c_ind):
            ind= tournament(population)
            if (best==[] or len(best)==1):
                best.append(ind)
            elif (fitness(ind)>fitness(best[i])):
                best[i] = ind
    return best 

def crossover(p1,p2):
    begin = random.randint(0,len(p1)-1)
    end = random.randint(0,len(p1)-1)

    if begin > end:
        begin,end = end,begin
    
    kid1 = p1[:begin] + p2[begin:end] + p1[:end]
    kid2 = p2[:begin] + p1[begin:end] + p2[:end]

    return kid1,kid2

def mutate(chromosome, probability):
    if random.random() <= probability:
        first = random.randint(0, len(chromosome) - 1)
        second = random.randint(0, len(chromosome) - 1)
        if first < second:
            chromosome[first: second + 1] = reversed(chromosome[first: second + 1])
        else:
            chromosome[second: first + 1] = reversed(chromosome[second: first + 1])
    return chromosome

def genbaru(generation=100,n_pop=100):
    pop = population(10,10)
    fitness = fitness(10)
    best_fit = -np.inf

    for i in range(generation):
        for j in range(n_pop):
            population[j].fitness(krom)

        population.sort()


def main():
    krom = chromosome(10)
    pop = population(10,10)
    p1,p2 = selectParents(10,pop)
    k1,k2 = crossover(p1,p2)
    kid = k1,k2
    print("kromosom        : ",krom)
    print ("Populasi        : ",pop)   
    print("x1,x2           :  ",decodeK(krom))
    print ("fitness         : ",fitness(krom))
    print("parent          : ",selectParents(10 ,pop))
    print ("kid             : ",decodeK(k1),decodeK(k2))
    print ("mutasi          : ",mutate(krom,0.05))
    



if __name__ == "__main__":
        main()