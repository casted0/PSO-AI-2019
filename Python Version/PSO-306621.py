import random as rand
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Variables for representing g_best

    x_dot = []
    y_dot = []

    # Array's shape (Dimensions)

    x       = 20
    dim     = 2

    # Arrays
    # numpy.empty(shape, dtype=float, order='C'), returns initialized and empty array
    # shape = (i, j)

    arr      = np.empty((dim, x)) # Array of particles
    vel      = np.empty((dim, x)) # Array of velocities
    p_best   = np.empty((dim, x)) # Personal best
    g_best   = np.empty((1, 2))   # Group best
    fitness  = np.empty((x))      # Result (Fitness solving the problem)

    # Initialize 
    # Personal best = Randomized
    # One personal best for each particle
    # Set velocity to 0

    for i in range(0, dim):

        for j in range(0, x):

            p_best[i][j] = rand.randint(-20, 20)
            arr[i][j] = p_best[i][j]
            vel[i][j] = 0

    
    # Calculate fitness with the random numbers initialized

    for i in range(0, x):

        fitness[i] = calc_fitness(arr[0][i], arr[1][i])


    # Get elements from personal best and the fitness in numerical order

    bubble_short(p_best, fitness, x)

    # Set the Group best from the p_best array
    # Position [0][0] and [1][0] after bubble sort

    g_best[0][0] = p_best[0][0]
    g_best[0][1] = p_best[1][0]

    plt.ion()
    fig  = plt.figure()
    axis = fig.add_subplot(111)
    axis.grid(True)

    for i in range(150):

        for j in range(x):

            # Calculate personal best

            if(calc_fitness(arr[0][j], arr[1][j]) < calc_fitness(p_best[0][j], p_best[1][j])):
                p_best[0][j] = arr[0][j]
                p_best[1][j] = arr[1][j]

            # Calculate group best

            if(calc_fitness(p_best[0][j], p_best[1][j]) < calc_fitness(g_best[0][0], g_best[0][1])):
                g_best[0][0] = p_best[0][j]
                g_best[0][1] = p_best[1][j]

            # Calculate velocity

            calc_velocity(x, arr, p_best, g_best, vel)

        l1 = axis.plot(arr[0], arr[1], 'r+')
        l2 = axis.plot(g_best[0][0], g_best[0][1], 'g*')
        axis.set_xlim(-10, 10)
        axis.set_ylim(-10, 10)
        fig.canvas.draw()
        axis.clear()
        axis.grid(True)
            
        print '[' + str(i) + ']' + ' Best Group fitness found: ' + str(g_best)

        x_dot.append(i)
        y_dot.append(g_best[0][0] * -1)

    print 'Best fitness found: '
    print g_best

    plt.plot(x_dot, y_dot)
    plt.xlabel('Generation')
    plt.ylabel('g_best')
    plt.title('Best fitness found over generations')
    plt.savefig('g_best.png')
    plt.show()


# Function used to calculate the fitness

def calc_fitness(x, y):

        # 100 * ((y - (x ^ 2)) ^ 2) + ((1 - (x ^ 2)) ^ 2)

        return 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)


# Function used to sort fitness array and particles positions

def bubble_short(p_best, fitness, x):
    
    for i in range(1, x):

        for j in range(0, x - 1):

            if fitness[j] > fitness[j + 1]: # If element i > element i+1 then swap
                
                aux = fitness[j]
                fitness[j] = fitness[j + 1]
                fitness[j + 1] = aux

                aux = p_best[0][j]
                p_best[0][j] = p_best[0][j + 1]
                p_best[0][j + 1] = aux

                aux = p_best[1][j]
                p_best[1][j] = p_best[1][j + 1]
                p_best[1][j + 1] = aux


def calc_velocity(x, arr, p_best, g_best, vel):

    for i in range(x):

        #Velocidad en X

        vel[0][i] = 0.7 * vel[0][i] + (p_best[0][i] - arr[0][i]) * rand.random() * 1.47 + (g_best[0][0] - arr[0][i]) * rand.random() * 1.47
        arr[0][i] = arr[0][i] + vel[0][i]

        #Velocidad en Y

        vel[1][i] = 0.7 * vel[1][i] + (p_best[1][i] - arr[1][i]) * rand.random() * 1.47 + (g_best[0][1] - arr[1][i]) * rand.random() * 1.47
        arr[1][i] = arr[1][i] + vel[1][i]


if '__main__' == main():

    main()