#coding:utf-8
#test
#1. import pylint, then normal outputs(and set conf).
import pylint.lint

#2. import pylint, then get the strand-outputs and error-info (in silence).
#from pylint import epylint as lint

# *args == opts
def pycheck(filepath, *args):
    '''
    pycheck(filepath, *args)
    
        the first params "filepath"<type:string> is the path which will be open.
        the second params "*args"<type:string> can be "-sn(y) / --score=n(y)", "-rn(y) / --report=n(y)" or None.
    '''
    #1.
    if args:
    #[NOTE]Don't need 'open'
        pylint_opts = ['%s'%args[0], '%s'%filepath]
        pylint.lint.Run(pylint_opts)
    else:
        pylint_opts = ['%s'%filepath]
        pylint.lint.Run(pylint_opts)
    #2.
    #(pylint_stdout, pylint_stderr) = lint.py_run('betest.py', return_std=True)

    #pylint.epylint.py_run()

    #print(pylint_stdout.read())#, pylint_stderr.read())
    #return pylint_stdout, pylint_stderr

if __name__ == '__main__':
    
    filepath = 'betest.py'
    pycheck(filepath)
