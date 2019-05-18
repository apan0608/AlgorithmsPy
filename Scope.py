# This flle talks about scope and namespace rules in PYthon
# https://docs.python.org/3/tutorial/classes.html
# scope: innermost scope, scope of functions,  current module's global names, outermost(builtins)
# nonlocal to rebind variable found outside of the innermost scope, if not variables are readonly
# attempting to write will create a new variable in the innermost scope
# global statement, if no such statemetn, assignments to names go into the innermost scope
# assignments bind names to objects, del removes the binding to the namespace reference


def scope_test():
    def do_local():
        scope = "local scope"

    def do_nonlocal():
        nonlocal scope 
        scope = "nonlocal scope"

    def do_global():
        global scope
        scope = "global scope"

    print("hello")
    scope = "test scope"
    do_local() # will create a new variable,
    print(scope) # test scope
    do_nonlocal() # rebind variables from the innermost scope to the outside, 
    print(scope) # nonlocal scope 
    do_global() # rebound to golbal, it will look for it outside of scope_test method 
    print(scope) #  nonlocal scope, assigned to the global one not enclosed one 

scope_test()
print(scope) # global scope, was assigned by do_global() methodm. otherwise will have no variable

a = scope_test
a()
print(a())