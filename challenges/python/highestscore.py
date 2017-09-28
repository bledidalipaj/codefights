def HighestScore(game):
    """
        You and your friend are playing a game, where you are player one and he is player two. In this game, your task is to get the highest 
        possible score. Your opponents goal is to make your final score as small as possible.

        You are given a binary tree which represents the game. Each inner node of the tree represents a state of the game, and each leaf contains 
        an integer which represents the final score.

        After you make a move, your opponent makes a move that blocks one of your possible next moves.

        Your task is to find the maximum number of points you can get by the end of the game.

        Example

        For game = "[7, 1]", the output should be
        HighestScore(game) = 7.

        You make the first move and can instantly get to the leaf, which will give you 7 points.


        For game = "[[10,8],5]", the output should be
        HighestScore(game) = 8.

        At first, you should choose the left branch. Your opponent will then block branch 10 and leave you branch 8.



        Input/Output

        [time limit] 4000ms (py)
        [input] string game

        A string containing an array representing the game tree as a binary tree of nested binary decision nodes.

        Constraints:
        2 ≤ number_of_leafs ≤ 6000.

        [output] integer

        The highest possible score for Player # 1.

        # Challenge's link: https://codefights.com/challenge/nYRdtSE58ChzYbhEN/main #
    """
    res = game
    
    while '[' in res:
        open_bracket_indexes = []
        counter = 0
        
        for index, symbol in enumerate(res):
            if symbol == '[':
                open_bracket_indexes.append(index)
                counter += 1
            if symbol == ']':
                counter -= 1
                expr = res[open_bracket_indexes.pop(): index + 1]
                num_1, num_2 = re.findall(r'\d+', expr)
                
                if counter % 2 == 0:
                    res = res.replace(expr, str(max(int(num_1), int(num_2))))
                else:
                    res = res.replace(expr, str(min(int(num_1), int(num_2))))
                break
    return int(res)


def HighestScore(game):
    res = game
    
    while '[' in res:
        open_bracket_indexes = []
        
        for index, symbol in enumerate(res):
            if symbol == '[':
                open_bracket_indexes.append(index)
            if symbol == ']':
                expr = res[open_bracket_indexes.pop(): index + 1]
                num_1, num_2 = re.findall(r'\d+', expr)
                
                if len(open_bracket_indexes) % 2 == 0:
                    res = res.replace(expr, str(max(int(num_1), int(num_2))))
                else:
                    res = res.replace(expr, str(min(int(num_1), int(num_2))))
                break
    return int(res)


import ast

def HighestScore(game):
    def makeTurn(tree, isPlayer1=True):
        vals = []
        
        for node in tree:
            if isinstance(node, list):
                vals.append(makeTurn(node, not isPlayer1))
            else:
                vals.append(node)
        if isPlayer1:
            return max(vals)
        else:
            return min(vals)

    return makeTurn(ast.literal_eval(game))


def HighestScore(game):
    import ast
    game = ast.literal_eval( game)
    
    def runDownTree(tree, player):
        if type(tree) == int:
            return tree
        
        lBest = runDownTree( tree[0], 1-player )
        rBest = runDownTree( tree[1], 1-player )
        
        if player == 1:
            return min(lBest, rBest)
        else:
            return max(lBest, rBest)
        
    return runDownTree( game, 0)

# aka minimax
def HighestScore(game):
    game = eval(game)
    def max_value(game):
        if isinstance(game, (int, long)): return game
        v = -float("inf")
        for a in game:
            v = max(v, min_value(a))
        return v

    def min_value(game):
        if isinstance(game, (int, long)): return game
        v = float("inf")
        for a in game:
            v = min(v, max_value(a))
        return v

    return max_value(game)