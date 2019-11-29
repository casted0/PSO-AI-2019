#include "Particle.h"

/**
 * 
 * Particle.c: File that contains all the working functions and structure of particles
 * 
 */

struct _Position
{
    double x_cord;
    double y_cord;
};

struct _Particle 
{
	Position act_pos;
    Position best_pos;
    double velocity;
    double inertia;
};


Particle * particle_create(){

    Particle * aux = NULL;
    Position p_aux = {-1, -1};

    aux = (Particle*)malloc(sizeof(Particle));

    if(aux == NULL){
        printf("Memory could not be allocated for the Particle.\n");
        return NULL;
    }

    aux->act_pos  = p_aux;
    aux->best_pos = p_aux;
    aux->velocity = -1;
    aux->inertia = -1;

    return aux;

}


void particle_destroy(Particle * p){

    if(p != NULL){
        free(p);
    }

}

void particle_set_velocity(Particle * p, double v){

    if(p != NULL){
        p->velocity = v;
    }

}

double particle_get_velocity(Particle * p){

    if(p != NULL){
        return p->velocity;
    }

}

void particle_set_inertia(Particle * p, double v){

    if(p != NULL){
        p->inertia = v;
    }

}

double particle_get_inertia(Particle * p){

    if(p != NULL){
        return p->inertia;
    }

}

void particle_set_position(Particle * p, Position pos){

    if(p != NULL){
        p->act_pos = pos;
    }

}

Position particle_get_position(Particle * p){

    if(p != NULL){
        return p->act_pos;
    }

}

void particle_set_best_position(Particle * p, Position pos){

    if(p != NULL){
        p->best_pos = pos;
    }

}

Position particle_get_best_position(Particle * p){

    if(p != NULL){
        return p->best_pos;
    }

}

void particle_print(Particle * p){

    if(p == NULL){
        printf("Particle is empty or non-allocated\n");
        return;
    }

    printf("Particle actual position: [%lf, %lf]\n", p->act_pos.x_cord, p->act_pos.y_cord);
    printf("Particle best position:   [%lf, %lf]\n", p->best_pos.x_cord, p->best_pos.y_cord);
    printf("Particle velocity:             [%lf]\n", p->velocity);
    printf("Particle inertia:              [%lf]\n", p->inertia);

}