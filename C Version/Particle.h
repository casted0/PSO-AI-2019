#ifndef PARTICLE_H
#define PARTICLE_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/**
 * 
 * Particle.h: Header file for Particle data type
 * 
 */

typedef struct _Particle Particle;                                      // Particles of the swarm
typedef struct _Position Position;                                      // Auxiliar structure for coordinates

Particle *  particle_create();                                          // Function for allocating memory for the particle and basic initialization

void        particle_destroy(Particle * p);                             // Function for destroying allocated memory for a particle

void        particle_set_velocity(Particle * p, double v);              // Function for setting velocity

double      particle_get_velocity(Particle * p);                        // Function for getting velocity

void        particle_set_inertia(Particle * p, double v);              // Function for setting inertia

double      particle_get_inertia(Particle * p);                        // Function for getting inertia

void        particle_set_position(Particle * p, Position pos);          // Function for setting the actual position

Position    particle_get_position(Particle * p);                        // Function for getting the actual position

void        particle_set_best_position(Particle * p, Position pos);     // Function for setting the best position

Position    particle_get_best_position(Particle * p);                   // Function for getting the best position

void        particle_print(Particle * p);                               // Function for printing the attributes of the particle (Mostly debugging)

#endif