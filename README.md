# PSO-AI-2019
Repository for Artificial Intelligence course final project, Particle Swarm Optimization algorithm (PSO)

INFORMATION RETRIEVED FROM: https://nathanrooy.github.io/posts/2016-08-17/simple-particle-swarm-optimization-with-python/

# Particle Position

X  = Particle's position
V  = Particle's velocity
K  = iteration


X(k+1) = X(k) + V(k+1);


# Particle Velocity

X  = Particle's position
V  = Particle's velocity
PI = Best individual particle position
PG = Best Swarm's position
W  = Constant inertia weight
C1 = Cognitive parameter
C2 = Social parameter
R1 = Random number #1 (Between 0 and 1)
R2 = Random number #2 (Between 0 and 1)
K  = Iteration


V(k+1) = W(k)*V(k) + C1*R1*(PI(k) - X(k)) + C2*R2*(PG(k) - X(k));