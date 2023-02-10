import numpy as np

# Define the states
states = ["Offense", "Defense", "Transition"]

# Define the transition probabilities
transition_probabilities = np.array([[0.8, 0.1, 0.1],
                                      [0.3, 0.5, 0.2],
                                      [0.2, 0.4, 0.4]])

# Create the transition matrix
transition_matrix = np.zeros((len(states), len(states)))
for i in range(len(states)):
    transition_matrix[i, :] = transition_probabilities[i, :] / sum(transition_probabilities[i, :])

# Simulate the game
current_state = 0
num_steps = 100
state_history = [current_state]
for i in range(num_steps):
    next_state = np.random.choice(states, p=transition_matrix[current_state, :])
    state_history.append(next_state)
    current_state = next_state