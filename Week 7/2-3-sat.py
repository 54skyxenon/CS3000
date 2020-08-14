#!/usr/local/bin/python3
# Author: Brandon Liang

# Negate a variable symbol
def negate(var):
    if var[0] == '~':
        return var[1:]
    else:
        return '~' + var

# Formula class to make parsing easier for 2-SAT
class TwoSATFormula:
    def __init__(self, expression):
        self.vars = set(expression) - {'(', ')', '^', ' ', 'v', '~'}
        self.clauses = [tuple(e[1:-1].split(' v ')) for e in expression.split(' ^ ')]

    # Return a set of all variables in this expression
    def getVars(self):
        return self.vars

    # Return list of all clauses' variables
    def getClauses(self):
        results = []
        for c in self.clauses:
            results.append((negate(c[0]), c[1]))
            results.append((negate(c[1]), c[0]))

        return results

    def evaluate(self, args):
        raise NotImplementedError('You don\'t need to evaluate an expression for 2-SAT!')

# Formula class to make parsing easier for 3-SAT
class ThreeSATFormula(TwoSATFormula):
    def __init__(self, expression):
        super().__init__(expression)

    # Return list of all clauses' variables
    def getClauses(self):
        results = []
        for c in self.clauses:
            results.append((c[0], c[1], c[2]))

        return results

    # Evaluate a specific boolean expression
    def evaluate(self, args):
        def atomicEval(var):
            if var[0] == '~':
                return not args[var[1:]]
            else:
                return args[var]

        result = True
        clauses = self.getClauses()

        for clause in clauses:
            result = result and any([atomicEval(c) for c in clause])

        return result

    # Is this formula satisfiable?
    def isSatisfiable(self, permutation, vars):
        if not vars:
            return self.evaluate(permutation)
        else:
            truePossibility, falsePossibility = dict(permutation), dict(permutation)
            truePossibility[vars[0]] = True
            falsePossibility[vars[0]] = False

            nextIsTrue = self.isSatisfiable(truePossibility, vars[1:])
            nextIsFalse = self.isSatisfiable(falsePossibility, vars[1:])

            return nextIsTrue or nextIsFalse
            

# 2-SAT: Is there an assignment of variables that satisfies a formula of 2-clauses ANDed together
# 2-SAT is both solvable in polynomial time (P) and verifiable in polynomial time (P)
# The time complexity specifically for 2-SAT is O(n^3), for n variables

def twoSAT(expression):
    formula = TwoSATFormula(expression)
    vars, clauses = formula.getVars(), formula.getClauses()

    graph = dict()

    for var in vars:
        graph[var] = set()
        graph['~' + var] = set()

    for clause in clauses:
        graph[clause[0]].add(clause[1])

    def DFS(current, target, visited):
        if current == target:
            return True
        elif graph[current].issubset(visited):
            return False
        else:
            for out in graph[current]:
                visited.add(out)
            return any([DFS(out, target, visited) for out in graph[current]])
        
    satisfiable = not any([DFS(var, negate(var), {var}) and DFS(negate(var), var, {negate(var)}) for var in vars])
    return expression + (' can' if satisfiable else ' cannot') + ' be satisfied'


# 3-SAT: 2-SAT, except with 3-clauses
# 3-SAT verifiable in polynomial time (P), but we don't know if it's solvable in polynomial time (NP)
# In other words, does P = NP?
# The time complexity specifically for this brute force 3-SAT is O(m * 2^n), for n variables and m clauses

def threeSAT(expression):
    formula = ThreeSATFormula(expression)
    satisfiable = formula.isSatisfiable(dict(), list(formula.getVars()))
    return expression + (' can' if satisfiable else ' cannot') + ' be satisfied'

print(twoSAT('(a v ~b) ^ (b v c) ^ (~a v d) ^ (~d v ~c)'))
print(twoSAT('(a v ~b) ^ (~b v c) ^ (~a v d) ^ (~d v ~c)'))
print(twoSAT('(a v ~b) ^ (~a v b) ^ (~a v ~b) ^ (a v b)'))

print(threeSAT('(a v b v c) ^ (~a v ~b v c) ^ (a v ~b v ~c) ^ (~a v b v ~c)'))
print(threeSAT('(x v y v z) ^ (x v y v ~z) ^ (x v ~y v z) ^ (x v ~y v ~z) ^ (~x v y v z) ^ (~x v y v ~z) ^ (~x v ~y v z) ^ (~x v ~y v ~z)'))