#! /bin/python
# Dark Horizon SConstruct file
import subprocess, sys, os
import platform
import glob
import shlex
import shutil

from colorizer import colorizer
from BuildHelper import *

setup(ARGUMENTS)



def setupDependencies():
	### Set our libraries
	print()

def setupEnvironment(env):
	col = colorizer()
	col.colorize(env)
	
	### Set our environment variables
	env.Append( CPPFLAGS = cpp_flags )
	env.Append( CPPDEFINES = cpp_defines )
	env.Append( CPPPATH = cpp_paths )
	env.Append( LINKFLAGS = link_flags )
	
	env.SetOption('num_jobs', multiprocessing.cpu_count())



### Clear the screen
clear()
if (not isWindows):
	os.system( 'echo' )
	os.system( 'echo' )
	os.system( 'echo' )


print("Compiling Accidental Noise")

# Tell SCons to create our build files in the 'build' directory
VariantDir('build', 'src', duplicate=0)

# Set our source files
source_files = Glob('build/*.cpp')
#source_files = Glob('include/*.h')

setupDependencies()

### Create our environment
env = Environment(ENV = os.environ, TOOLS = [compiler])
setupEnvironment(env)

print("Build type: " + buildFlags['buildType'])

# Tell SCons the program to build
env.StaticLibrary('build/accidentalnoise', source_files, LIBS = libraries, LIBPATH = library_paths)
