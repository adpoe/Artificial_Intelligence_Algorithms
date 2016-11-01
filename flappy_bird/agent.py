from collections import defaultdict
import markov_decision_process as mdp
import random
import itertools

# TODO: Implement save and reload functions
# TODO: Implement Exploration function

class QLearningAgent:
    # state space = (bird_height, pipe_bottom_y, pipe_dist, pipe_collision)
    # reward = if no collision +1, if collision -1000
    #
    # THINK:
    #   * bird height - pipe_bottom_y can discretized into 3 buckets
    #       0 = close  ( y < 100 )
    #       1 = mid    ( 100 < y < 200 )
    #       2 = far    ( 200 < y )
    #   * same thing for pipe dist
    #       0 = close  ( x < 100 )
    #       1 = mid    ( 100 < x < 200 )
    #       2 = far    ( 200 < x )

    #  now need a way to grab all this information...
    #  initialize an agent and pass the bird and pipes to it each time we start an episode
    #  so --> run episode needs to take an argument, and that argument is the Q-LearningAgent
    #  and once we initialize the pipes and bird, we pass those values into the Q-LearningAgent each time

    #  if each of these 3 buckets were crossed with each other, how many total states would we have?
    #  these are the nodes from each level of our tree.
    #  can use this --> nodes = list(itertools.product( (0,1,2) , repeat=2))
    #           gives 9 nodes to search through, discretely at each step... or does it...
    #  they aren't really nodes... they're possible states... and we only have two options (nodes)
    #        Node 1 = Stay
    #        Node 2 = Jump
    #  and we can store data into our Q-Learning agent based on those 9 discrete spaces
    #  depending on which state we are in, we store our statistics for the step in that particular node.
    #  or not -- each of thee are nodes, i think...
    #  Okay, so -->
    #       nodes = list(itertools.product( (0,1,2) , repeat=2))
    #       STATE_ACTION_PAIRS = state_action_pairs = list(itertools.product(nodes, ('S', 'J')))


    def __init__(self):
        """,mdp, bird, pipes, pp"""
        # need to set these each new episode
        self.bird = None #bird   # set=bird
        self.pipes = None #pipes  # set=pipes
        self.pp = None #pp     # flappy's pipe info data structure

        # current state
        #self.current_state = self.observeState(self.bird, self.pipes, self.pp)
        self.current_state = None
        # time
        self.t = 0

        # Q-ARRAY
        self.q_data = {}
        s_a_pairs = self.generateStates() # get all state/action pairs
        # turn them all into strings and initialize our dictionary with them
        for elem in s_a_pairs:
            key = str(elem)
            self.q_data[key] = 0.0

        # agent-specific values
        self.gamma = 0.7
        """
        self.alpha = lambda n: 1./(1+n)
        """
        return

    def generateStates(self):
        """
        :return: Returns a list containing all discretized states for Flappy Bird proble
        """
        nodes = list(itertools.product( (0,1,2) , repeat=2))
        STATE_ACTION_PAIRS = state_action_pairs = list(itertools.product(nodes, ('S', 'J')))
        return state_action_pairs


    def observeState(self, bird, pipes, pp):
        # observe state flappy is in
        #  get info here --> and calculate reward after we check for collision....
        bird_height = bird.y
        pipe_bottom = 500 - pp.bottom_height_px
        pipe_dist = pp.x

        # first value in state tuple
        height_category = 0
        dist_to_pipe_bottom = pipe_bottom - bird.y
        if dist_to_pipe_bottom < 100:
            height_category = 0
        elif dist_to_pipe_bottom < 200:
            height_category = 1
        else:
            height_category = 2

        # second value in state tuple
        dist_category = 0
        dist_to_pipe_horz = pp.x - bird.x
        if dist_to_pipe_horz < 100:
            dist_category = 0
        elif dist_to_pipe_horz < 200:
            dist_category = 1
        else:
            dist_category = 2

        # check for collision
        pipe_collision = any(p.collides_with(bird) for p in pipes)
        collision = pipe_collision
        state = (height_category, dist_category, collision)
        return state

    def performAction(self, state):
        # perform action that maximizes expected reward
        actions = self.getActions(state)
        best_action = self.findMaxReward(actions)
        # send this action back to game space, and either it will say
        # 'MOUSEBUTTONUP', or nothing this turn
        # so, need to connect this to our game itself
        return best_action, state

    # then let clock tick
    def updateTime(self):
        self.t += 1

    # place after the get events part of loop in the game
    def collectReward(self, state, collision):
        # obverse new state and collect reward associated
        # +1 if alive
        # -1000 if dead
        reward = 1
        # if True in state:
        if collision:
            reward = -1000
        return reward

    def updateQArray(self, prev_state, action, reward):
        # update Q array according to the q-learning rule
        key = ((prev_state[0], prev_state[1]), action)
        self.q_data[str(key)] = reward + self.gamma * self.q_data[str(key)]
        return

    # place at bottom of loop
    def updateState(self):
        # set current state to s'
        self.current_state = self.observeState(self.bird, self.pipes, self.pp)
        return

    # and repeat the loop!

    #################################
    ####### MAIN LEARNING LOOP ######
    #################################
    # TODO: Implement LEARN! Chain it all together and start giving it a try. See how it goes.

    def newEpisode(self, bird, pipes):
        """
            Run this method each time we start a new episode
        """
        self.bird = bird
        self.pipes = pipes
        #self.pp = self.pipes[0]

    def newIteration(self):
        self.pp = self.pipes[0]

    def stepAndMakeChoice(self):
        # chain actions above all together
        #self.newEpisode(self.bird, self.pipes, self.pp)
        self.current_state = self.observeState(self.bird, self.pipes, self.pp)
        action,state = self.performAction(self.current_state)
        return action,state

    def learnFromChoice(self, action, prev_state, collision):
        self.updateTime()
        self.updateState()
        reward = self.collectReward(prev_state, collision)
        if reward < 1:
            print str(reward)
        self.updateQArray(prev_state, action, reward)


    ###############################
    ##### UTILITY FUNCTIONS #######
    ###############################
    def findMaxReward(self, actions):
        # find max reward predicted for all possible actions
        decision = 'S'
        # we know only two actions for flappy
        reward_jump = self.q_data[actions[0]]
        reward_stay = self.q_data[actions[1]]
        print "REWARD JUMP="+str(reward_jump)
        print "REWARD STAY="+str(reward_stay)
        if reward_jump > reward_stay:
            decision = 'J'

        return decision

    def getActions(self, state):
        # given a state, return a list containing possible actions
        # should only be 2 for Flappy Bird --> Jump or Stay
        t = (state[0], state[1])
        jump = str((t, 'J'))
        stay = str((t, 'S'))
        return [jump, stay]

