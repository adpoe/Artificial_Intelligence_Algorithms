import itertools

##########################
###### MINI-MAX A-B ######
##########################

class AlphaBeta:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.root  # GameNode
        return

    # Do an AB Search with cutoff at depth and time
    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print "AlphaBeta:  Utility Value of Root Node: = " + str(best_val)
        print "AlphaBeta:  Best State is: " + best_state.Name
        return best_state

    def max_value(self, node, alpha, beta):
        print "AlphaBeta-->MAX: Visited Node :: " + node.Name
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = -infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print "AlphaBeta-->MIN: Visited Node :: " + node.Name
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value
    #                     #
    #   UTILITY METHODS   #
    #                     #
    # ---> these need to be supported by the game class itself, going forward.

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value




#########################
###### GAME OBJECT ######
#########################

class Game:
    def __init__(self, board):
        self.initial_state = None
        self.current_state = None
        self.game_tree = None
        self.game_board = board.config
        self.board = board
        # player(s) --> who's the player in the state
        # successors(s) --> possible moves from current state
        # result(a,s) --> the resulting state after action (a) is taken on state (s)
        # terminal(s) --> returns true if state is a terminal state
        # utility(s,p) --> the value function of state (s) for player (p)

    def player(self, s):
        # given a state, determine current player
        # MAX or MIN
        return None

    def successors(self, s):
        # Given a current state, return a list of successor states
        return None

    def result(self, a, s):
        #
        return None

    def terminal(self, s):
        return None

    def utility(self, s, p):
        return None

    #                 #
    #     HELPERS     #
    #                 #
    def getSuccessorsBoard(self):
        # pass in board, get all possible queen moves for this turn...
        # every queen across every row, col, and diagonal.... so lots
        return None

    def getSuccessorsArrow(self):
        # pass in queen move and board, get all possible arrow shots
        return None

    #                 #
    #   SUB HELPERS   #
    #                 #
    def getQueenLocations(self):
        # get locations of all the queens
        # return  a list with locations in tuples, (y,x)
        # need to know whether you are Q or q though.... how?
        if self.board.bWhite:
            matchChar = 'Q'
        else:
            matchChar = 'q'

        queenList = []
        # get uppercase queens
        for row in xrange(0, len(self.game_board)):
            for col in xrange(0, len(self.game_board)):
                if self.game_board[row][col] == matchChar:
                    queenList.append((row, col))
        return queenList


    def getValidDiags(self, location):
        #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
        # create our list
        diagonalsList = []

        # store the board size, to make code simpler
        boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

        # ground the location so we know where we're starting from
        row = location[0]
        col = location[1]

        #--------------------------
        #   Bottom Left Diagonal
        #--------------------------
        # -1 row, -1 col
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r -= 1
            c -= 1

            # protect against out of bounds
            if r < 0 or c < 0:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                diagonalsList.append((r, c))

        #--------------------------
        #    Top Right Diagonal
        #--------------------------
        # +1 row, +1 col
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r += 1
            c += 1

            # protect against out of bounds
            if r > boardSize or c > boardSize:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                diagonalsList.append((r, c))

        #--------------------------
        #   Bottom Right Diagonal
        #--------------------------
        # -1 row, +1 col
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r -= 1
            c += 1
            # protect against out of bounds
            if r < 0 or c > boardSize:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                diagonalsList.append((r, c))

        #--------------------------
        #    Top Left Diagonal
        #--------------------------
        # +1 row, -1 col
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r += 1
            c -= 1
            # protect against out of bounds
            if r > boardSize or c < 0:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                diagonalsList.append((r, c))

        # return the list, now that we're all done
        return diagonalsList


    def getValidVerts(self, location):
        #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
        # create our list
        vertsList = []

        # store the board size, to make code simpler
        boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

        # ground the location so we know where we're starting from
        row = location[0]
        col = location[1]

        #--------------------------
        #         Top Rows
        #--------------------------
        # row+1, col=same
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r += 1

            # protect against out of bounds
            if r > boardSize:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                vertsList.append((r, c))

        #--------------------------
        #        Bottom Rows
        #--------------------------
        # row-1, col=same
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            r -= 1

            # protect against out of bounds
            if r < 0:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                vertsList.append((r, c))

        # return the verticals we've found
        return vertsList


    def getValidHorz(self, location):
        #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
        # create our list
        horzList = []

        # store the board size, to make code simpler
        boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

        # ground the location so we know where we're starting from
        row = location[0]
        col = location[1]

        #--------------------------
        #       Right Cols
        #--------------------------
        # row=same, col+1
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            c += 1

            # protect against out of bounds
            if c > boardSize:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                horzList.append((r, c))

        #--------------------------
        #        Left Cols
        #--------------------------
        # row=same, col-1
        r = row
        c = col
        valid = True
        while valid:
            # update the row/col values
            c -= 1

            # protect against out of bounds
            if c < 0:
                break

            # pull out the value
            v = self.game_board[r][c]
            if not v == '.':
                break
            # otherwise, we have a '.', and the cell is valid
            else:
                horzList.append((r, c))

        # return the verticals we've found
        return horzList

    # Location (x,y) -> [ Locations ]
    def getValidMoves(self, location_tuple):
        """
        General method to get all valid 'moves' from some (y,x) coord
        :param location_tuple: (y,x)
        :return: a list of location tuples
        """
        # given queen location-->OR<--an arrow location, find all valid moves
        # for all the elements...
        diags = self.getValidDiags(location_tuple)
        verts = self.getValidVerts(location_tuple)
        horz = self.getValidHorz(location_tuple)

        # concat them all
        validMoves = diags + verts + horz

        # build all queen moves from current step
        # pass in all queen moves and concat on the possible arrow moves to each
        # that list is the return value
        return validMoves

    # [Queen Locations (y,x)] -> [(Location, [All Locations])
    def getAllFutureQueenLocations(self, queenLocations):
        """
        Take the list of current queen locations, and output a list that contains
        [ (Queen Location Now, [ All Possible Future Locations in next Move) ]
        @param list of queen locations
        :return:  List with the queen location and all possible future locations
        """
        # (x,y) -> ( (x,y), [(x,y) .... ])
        future_locations = []

        # get all valid moves for each queen
        for elem in queenLocations:
            # grab the moves
            validMoves = self.getValidMoves(elem)
            # then make a tuple containing (cur_location, [future locations])
            move_tuple = (elem, validMoves)
            # and add that tuple to our list
            future_locations.append(move_tuple)


        # THINK: later we can map the first location of over the future locations
        #        then same thing with arrow locations but

        return future_locations

    # [Queen Location, [All Locations]] -> [Queen Location, [(All Locations, Arrow Show)])
    def getArrowLocations(self):
        return None

    # --> this is like concatting arrow locations with the dest locations
    # Queen Location (y,x) -> [(src_loc, dst_loc, arrow_loc)]
    def getAllMovesForQueen(self):
        # (y,x) -> [ Locations ] ... pull out each location
        # and for get all arrow locations for each
        # make a new tuple from the arrow locations.... and concat all those as well
        return None

    # Board -> [ All Queen Locations ]
    def getAllMovesPossible(self, location_tuple):
        # get location moves, and for each, get the arrow move
        # put the arrow move in the last elem of location move
        return None

    def BuildMoveTree(self):
        # build one level of tree.
        return

    def AddTreeLevel(self):
        return