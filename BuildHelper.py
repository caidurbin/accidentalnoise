import subprocess, sys, os
import platform
import multiprocessing

from SCons.Script import *

### Establish our system
isLinux = platform.system() == 'Linux'
isWindows = os.name == 'nt'
isMac = platform.system() == 'Darwin'

### Compiler
compiler = 'default'

buildFlags = {}
buildFlags['debug'] = True # True by default (at least for now)
buildFlags['useCef'] = True
buildFlags['beautify'] = False
buildFlags['clean'] = False
buildFlags['buildType'] = 'debug'

cpp_paths = []
cpp_defines = []
cpp_flags = []
link_flags = []
library_paths = []
libraries = []



def setup(ARGUMENTS):	
	### Error check our platform type
	if (not isLinux and not isWindows and not isMac):
		print("Sorry, but it appears your platform is not recognized.")
		sys.exit(1)
	
	global buildFlags
	
	### Get our arguments
	compiler = ARGUMENTS.get('compiler')
	buildFlags['buildType'] = ARGUMENTS.get('buildType')
	
	### Set and error check our build flags
	if (GetOption('clean') is True):
		buildFlags['clean'] = True
	
	if (buildFlags['buildType'] is None or buildFlags['buildType'] == ''):
		buildFlags['buildType'] = 'debug'
	
	if ( buildFlags['buildType'] == 'debug' ):
		buildFlags['debug'] = True
	elif ( buildFlags['buildType'] == 'release' ):
		buildFlags['debug'] = False
	else:
		print( "Invalid build type!" )
		print( "Valid types are 'debug' or 'release'." )
		sys.exit(1)
	
	if (buildFlags['debug']):
		cpp_defines.append('DEBUG')
	
	if (compiler is None or compiler == ''):
		compiler = 'default'
	if (compiler == 'gcc' and isWindows):
		compiler = 'mingw'
	if (compiler == 'msvc' and isWindows):
		compiler = 'default'
	
	### Error check compiler
	if (compiler == 'msvc' and not isWindows):
		print( "Cannot use msvc in this environment!" )
		sys.exit(1)
	
	### Include the accidental noise .h files
	cpp_paths.append('include')
	
	### Set our OS specific compiler variables
	if (not isWindows):
		if (compiler == 'gcc' or (compiler == 'default' and isLinux)):
			if (buildFlags['debug']):
				cpp_flags.append('-g')
				cpp_flags.append('-O0') # optimization level 0
				cpp_flags.append('-pg') # profiler
			else:
				cpp_flags.append('-O3') # optimization level 3
			
			cpp_flags.append('-std=c++11')
			cpp_flags.append('-pedantic-errors')
			#cpp_flags.append('-Wall')
			#cpp_flags.append('-Wextra')
			#cpp_flags.append('-Werror')
		
	else:
		if isWindows:
			if (compiler == 'default'):
				cpp_flags.append('/w') # disables warnings (Windows)
				cpp_flags.append('/wd4350') # disables the specific warning C4350
				cpp_flags.append('/EHsc') # Enable 'unwind semantics' for exception handling (Windows)
				cpp_flags.append('/MD')
				
				if (buildFlags['debug']):
					cpp_flags.append('/Zi') # Produces a program database (PDB) that contains type information and symbolic debugging information for use with the debugger.
					cpp_flags.append('/FS') # Allows multiple cl.exe processes to write to the same .pdb file
					link_flags.append('/DEBUG') # Enable debug during linking
					cpp_flags.append('/Od') # Disables optimization
				else:
					cpp_flags.append('/Ox') # Full optimization
			elif (compiler == 'mingw'):
				if (buildFlags['debug']):
					cpp_flags.append('-g')
					cpp_flags.append('-O0') # optimization level 0
					cpp_flags.append('-pg') # profiler
				else:
					cpp_flags.append('-O3') # optimization level 3
				
				cpp_flags.append('-std=c++11')
				cpp_flags.append('-pedantic-errors')

def clear():
	if (isWindows):
		os.system('cls')
	else:
		os.system('clear')

def exitOnError(returnCode):
	if ( returnCode != 0):
		print( "Script halted due to error(s)!" )
		sys.exit(1)
